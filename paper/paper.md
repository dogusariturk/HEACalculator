---
title: 'HEACalculator: An Open-Source Python Tool for Thermodynamic Property Calculation and Solid Solution Prediction in High-Entropy Alloys'
tags:
  - Python
  - materials science
  - high-entropy alloys
  - computational thermodynamics
  - solid solution prediction
  - alloy design
authors:
  - name: Doğuhan Sarıtürk
    orcid: 0000-0003-0008-1165
    corresponding: true
    affiliation: 1
  - name: Yunus Eren Kalay
    orcid: 0000-0002-5514-5202
    affiliation: 2
  - name: Raymundo Arróyave
    orcid: 0000-0001-7548-8686
    affiliation: "1, 3, 4"
affiliations:
  - index: 1
    name: Department of Materials Science and Engineering, Texas A&M University, USA
    ror: 01f5ytq51
  - index: 2
    name: Department of Metallurgical and Materials Engineering, Middle East Technical University, Turkey
    ror: 014weej12
  - index: 3
    name: J. Mike Walker '66 Department of Mechanical Engineering, Texas A&M University, USA
    ror: 01f5ytq51
  - index: 4
    name: Wm Michael Barnes '64 Department of Industrial and Systems Engineering, Texas A&M University, USA
    ror: 01f5ytq51
date: 13 September 2026
bibliography: paper.bib
---

# Summary

High-entropy alloys (HEAs) have attracted sustained interest since their introduction by @cantor2004 and @yeh2004 because multi-principal-element compositions can exhibit unusual combinations of strength, thermal stability, and functional performance [@george2019; @miracle2017]. A recurring problem in HEA design is determining whether a candidate composition will form a single-phase solid solution or separate into multiple phases or intermetallic compounds. The answer decides which compositions are worth detailed thermodynamic analysis and experimental work, so it is asked early in alloy design.

`HEACalculator` is an open-source Python package that calculates the thermodynamic and structural descriptors used in HEA research and evaluates published solid-solution formation rules against them. It computes sixteen commonly used quantities, including mixing enthalpy, configurational entropy, valence electron concentration, Hume-Rothery electron-to-atom ratio, atomic size mismatch, electronegativity mismatch, and derived stability parameters such as Omega, Lambda, and Phi, and it evaluates eight published prediction criteria [@yang2012; @guo2013; @wang2015; @singh2014; @ye2015scr; @troparevsky2015; @senkov2016; @king2016]. It ships with a curated elemental and binary-interaction dataset and has three access modes. Users can work from a command-line interface (CLI), a desktop graphical user interface (GUI), or a Python application programming interface (API) for use in notebooks and screening scripts.

# Statement of Need

The phenomenological criteria for solid-solution formation in HEAs come from separate papers, each with its own notation, parameter definitions, and validation set. Anyone who wants to compare these models or reuse them in an automated study ends up re-implementing overlapping calculations and re-assembling the supporting data, and small differences between implementations are easy to miss. Routine composition screening becomes harder than it should be, and results are challenging to compare across studies.

Those papers list more than 300 compositions between them. The eight criteria give an answer for nearly all of them, but they rarely agree. Where they disagree, four in five split three ways, calling the same alloy a solid solution, an intermetallic, and multiple phases. AlCoCrFeNi is typical, with two criteria reporting a solid solution, two an intermetallic, and four multiple phases. Which criterion a study picks therefore usually determines the answer it reports. No criterion has emerged as the most reliable, so there is no good reason to report one and drop the others.

+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| **Symbol**                  | **Parameter**                                                | **Formula**                                                                      | **Unit**        |
+:============================+:=============================================================+:=================================================================================+:================+
| $\rho$                      | Density                                                      | $\sum w_i c_i / \sum V_i c_i$                                                    | g/cm$^3$        |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $T_m$                       | Melting temperature                                          | $\sum c_i T_{m,i}$                                                               | K               |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Delta H_\text{mix}$       | Mixing enthalpy                                              | $4\sum_{i<j} c_i c_j H_{ij}^\text{mix}$                                          | kJ/mol          |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Delta S_\text{mix}$       | Mixing entropy                                               | $-R\sum c_i \ln c_i$                                                             | J/(K$\cdot$mol) |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Delta H_f$                | Formation enthalpy                                           | $4\sum_{i<j} c_i c_j H_{ij}^f$                                                   | meV/atom        |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\min(\Delta H_f)$          | Minimum binary formation enthalpy                            | $\min_{i<j}(H_{ij}^f)$                                                           | meV/atom        |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| VEC                         | Valence electron concentration                               | $\sum c_i \text{VEC}_i$                                                          | ---             |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $e/a$                       | Hume-Rothery electron-to-atom ratio                          | $\sum c_i (e/a)_i$                                                               | ---             |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\delta$                    | Atomic size difference                                       | $100\sqrt{\sum c_i(1-r_i/\bar{r})^2}$                                            | %               |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\delta_\text{CN12}$        | Atomic size difference (CN12)                                | same formula, Goldschmidt CN12 radii                                             | %               |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Delta\chi_\text{Allen}$   | Electronegativity difference (Allen)                         | $100\sqrt{\sum c_i(1-\chi_i/\bar{\chi})^2}$                                      | %               |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Delta\chi_\text{Pauling}$ | Electronegativity difference (Pauling)                       | same formula, Pauling scale                                                      | %               |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\Omega$                    | Omega                                                        | $T_m \Delta S_\text{mix} / \lvert\Delta H_\text{mix}\rvert$                      | ---             |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\gamma$                    | Gamma                                                        | $\Omega_S / \Omega_L$                                                            | ---             |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\lambda$                   | Lambda                                                       | $\Delta S_\text{mix} / \delta^2$                                                 | J/(K$\cdot$mol) |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+
| $\varphi$                   | Phi                                                          | $(\Delta S_\text{mix} - \lvert\Delta H_\text{mix}\rvert/T_m) / \lvert S_E\rvert$ | ---             |
+-----------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------+

: Thermodynamic and structural descriptors computed by `HEACalculator` for a candidate alloy composition. Here $c_i$, $w_i$, and $V_i$ are the atomic fraction, atomic weight, and atomic volume of element $i$. The averages $\bar{r}$ and $\bar{\chi}$ are composition-weighted, $R$ is the gas constant, $S_E$ is the hard-sphere excess entropy [@ye2015int], and $\Omega_S$ and $\Omega_L$ are the solid angles subtended by the smallest and largest atoms. The atomic radius $r_i$ applies to $\delta$, $\lambda$, and $S_E$, while $\delta_\text{CN12}$ and $\gamma$ use the Goldschmidt CN12 radius. \label{tab:descriptors}

+-------------------+----------------------------------------------------------------------------------+--------------------+
| **Model**         | **Solid-solution criterion**                                                     | **Reference**      |
+:==================+:=================================================================================+:===================+
| Crystal structure | $2.5 \leq$ VEC $\leq 3.5$: HCP; \                                                | [@guo2011]         |
|                   | VEC $\geq 8$: FCC; \                                                             |                    |
|                   | VEC $\leq 6.87$: BCC; \                                                          |                    |
|                   | otherwise: BCC+FCC                                                               |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 1                 | $\Omega \geq 1.1$ \                                                              | [@yang2012]        |
|                   | $\delta_\text{CN12} \leq 6.6\%$                                                  |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 2                 | $-11.6 < \Delta H_\text{mix} < 3.2$ kJ/mol \                                     | [@guo2013]         |
|                   | $\delta < 6.6\%$                                                                 |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 3                 | $\gamma < 1.175$                                                                 | [@wang2015]        |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 4                 | $\lambda > 0.96$; \                                                              | [@singh2014]       |
|                   | $0.24 \leq \lambda \leq 0.96$: multiple phases; \                                |                    |
|                   | $\lambda < 0.24$: intermetallic                                                  |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 5                 | $\varphi \geq 20$                                                                | [@ye2015scr]       |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 6                 | $\min(H_{ij}^f) > -T_\text{crit}\Delta S_\text{mix}$ \                           | [@troparevsky2015] |
|                   | $\max(H_{ij}^f) < 37$ meV/atom                                                   |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 7                 | $k_1 < \Omega(T_\text{ann})(1-k_2)+1$; \                                         | [@senkov2016]      |
|                   | $k_2=0.6$, $T_\text{ann}=0.55\,T_m$                                              |                    |
+-------------------+----------------------------------------------------------------------------------+--------------------+
| 8                 | $\Phi = \Delta G_\text{SS}/(-\lvert\Delta G_\text{max}\rvert) \geq 1$            | [@king2016]        |
+-------------------+----------------------------------------------------------------------------------+--------------------+

: Published criteria for solid-solution formation implemented in `HEACalculator`. The crystal-structure row predicts the expected phase (FCC, BCC, HCP, or mixed BCC+FCC) from the valence electron concentration. Models 1--8 each classify a composition as *Solid Solution*, *Intermetallic*, or *Multiple Phases* based on the stated threshold. Models 1 and 3 take $\delta$ and $\gamma$ from Goldschmidt CN12 radii, while Models 2, 4, and 5 use uncorrected radii. The Model 7 ratio $k_1$ is $\Delta H_f/\Delta H_\text{mix}$, with $\Delta H_f$ in kJ/mol. Its parameters $k_2$ and $T_\text{ann}$ are user-configurable. The critical temperature $T_\text{crit}$ is $0.55\,T_m$, and $T_\text{crit}\Delta S_\text{mix}$ is converted to meV/atom. The Gibbs energies $\Delta G_\text{SS}$ and $\Delta G_\text{max}$ are those of the disordered solid solution and the largest-magnitude ordered binary. \label{tab:models}

`HEACalculator` computes the sixteen descriptors listed in \autoref{tab:descriptors} and implements all eight published criteria in one validated, reusable package (\autoref{tab:models}). It bundles a database of 118 elements, 2,628 binary mixing enthalpies from @takeuchi2005, and 435 binary formation enthalpies derived from density functional theory (DFT) data from @troparevsky2015, along with utilities for single-composition analysis, parameter sweeps, and batch processing. It is aimed at materials scientists doing exploratory alloy design or high-throughput screening, and at anyone preparing candidate compositions for experimental work.


# State of the Field

The closest peer among interactive screening tools is `HEAPS`, a free, open-source (CC0) HEA screening program that computes a larger collection of semi-empirical descriptors and criteria, including mechanical-property heuristics, through a MATLAB-based graphical workflow [@martin2022heaps]. It has two operating modes, a single-composition calculator and an exploration mode that screens large numbers of candidate alloys against user-defined composition and parameter constraints. Its standalone installer is built for 64-bit Windows and needs the free MATLAB Runtime, while running the MATLAB source files directly requires a MATLAB license. `HEACalculator`, by contrast, focuses more narrowly on the widely cited descriptors for solid-solution analysis, but packages them as a cross-platform, installable Python library with a documented API, command-line interface, and optional desktop GUI. That packaging lets other projects depend on the calculations and test them directly, on any operating system and without proprietary software.

`matminer` [@ward2018matminer] provides composition descriptors for materials informatics, including several alloy-specific featurizers, and leaves phase prediction to downstream models. Two HEA tools build such models. `AutomaticFeaturizerMPEA` [@subedi2022] is a Jupyter notebook that applies `matminer` featurizers to a dataset of multi-principal-element alloys, and the accompanying study trains a neural network on those features to detect intermetallic phases. `pyMPEALab` [@subedi2022pympealab] classifies phases through a graphical interface backed by a neural network. Both return a learned prediction rather than the verdicts of the published criteria. `HEACalculator` computes descriptors and then evaluates the eight published criteria against them. Each criterion reports its own verdict, so a user can see which rules a composition passes and which it fails.

The closest peer in library form is `hea-bench` [@fieser2026heabench], first released in 2026, seven years after `HEACalculator` was made public. It computes a similar descriptor set, applies nine empirical phase rules [@fieser2026heabenchsw], and extends both to high-entropy oxides. It works from a single radius tabulation, while `HEACalculator` carries two and gives each criterion the one its source paper used. The published thresholds were calibrated on particular radius sets and do not transfer between them. `hea-bench` has since added `HEACalculator` as an optional backend, as described in the Research Impact Statement.

Model-specific scripts and spreadsheet calculators distributed as supplementary material are convenient for reproducing a particular set of results, but they are not designed to be reused as dependencies. `HEACalculator` is versioned and tested, so other work can cite a specific release and build on it directly. Contributing to existing interactive tools would not remove the need for that programmatic capability.

# Software Design

`HEACalculator` is organized around a shared calculation core rather than around its user interfaces. A common parser normalizes compositions from the CLI, GUI, or Python API into one internal representation, which accepts compact formulas, explicit stoichiometries, and nested notation. The thermodynamic engine reads only that representation, so a composition gives the same result through any of the three interfaces. A separate prediction layer then applies the published thresholds to that one descriptor set.

The reference data ships as JSON inside the package, and each module records the source of the table it loads, so the provenance of every value is traceable from the code. When a required pair is missing, the data layer raises a typed exception rather than substituting a value. The calculation layer turns that into an `N/A` for the affected descriptor. Incomplete coverage stays visible, and users can tell an unsupported composition from a physically meaningful negative result.

![The `HEACalculator` graphical interface showing the HEA Parameters page. Users select elements from the periodic table, assign atomic-percent compositions, and calculate thermodynamic descriptors and solid-solution predictions in a single shared results view.\label{fig:gui}](figure_1.png)

Model 8 uses a different enthalpy model from the other criteria. Its two Gibbs energies follow the supplementary equations of @king2016 rather than the tabulated pair enthalpies used elsewhere in the package, applying the Miedema macroscopic-atom model with the parameterization of @deboer1988 and the structural term of @niessen1983. `HEACalculator` carries Miedema parameters for 35 elements, so Model 8 reports `N/A` when a composition contains an element outside that set. No other descriptor or criterion needs those parameters.

The test suite checks every model against the table of the paper that introduced it, more than 300 compositions in all. The descriptors reproduce the published values closely, and the criteria return the published phase label for roughly nine alloys in ten.

The architecture serves research use rather than only interactive exploration. The CLI screens a composition range across CPU cores in parallel and reads candidate alloys from a CSV file. The optional PyQt6 desktop application covers interactive use (\autoref{fig:gui}). The package works both as an end-user calculator and as a dependency inside a larger study.

# Research Impact Statement

`HEACalculator` has also been used as a descriptor source rather than as a phase-screening tool, supplying domain-specific features alongside general-purpose composition databases such as JARVIS [@choudhary2018jarvis; @choudhary2020jarvis], Oliynyk [@oliynyk2016], Magpie [@ward2016magpie], and mat2vec [@tshitoyan2019mat2vec]. Hossein @zadeh2024 combined those sources into 4937 candidate features and fitted an interpretable piecewise linear regression for the $\lambda_2$ compatibility parameter between the austenite and martensite phases of NiTi shape memory alloys, a quantity that correlates with transformation hysteresis. @sheikh2025 assembled 3372 features for Vickers hardness in refractory high-entropy alloys and narrowed them to six predictors through recursive feature elimination and mutual-information filtering. In each case the package supplied composition descriptors for a target property it does not itself predict, which is the reuse a packaged calculation core is meant to support.

`HEACalculator` has been publicly available since 2019. `hea-bench` [@fieser2026heabenchsw], an independently published calculator for HEAs and high-entropy oxides, pins it as an optional dependency and wraps its Python API in an adapter that maps fifteen descriptors onto its own names. Both packages compute eight of them, so a user can pick either implementation from the command line. The other seven come only from `HEACalculator`. The `hea-bench` documentation compares the two backends on the eight shared descriptors over a fixed panel of fifty compositions. Eight further quantities are left unmapped, among them the King Gibbs energies, the Ye $\phi$, and the excess entropy, because the two packages do not compute them the same way. That is the ambiguity described in the Statement of Need, reached independently by a group trying to make the two packages interoperate.

# AI Usage Disclosure

Claude Code (Anthropic, Claude Opus 5) and Codex (OpenAI, GPT-5) were used in the development of `HEACalculator` to draft docstrings and documentation, scaffold unit tests, and suggest refactorings of existing code, and to copy-edit this manuscript. The authors reviewed, edited, and validated all AI-assisted output before including it, accepting suggested code changes only after the full test suite passed, and are responsible for the correctness of the software, its documentation, and this paper.

# Acknowledgements

R.A. and D.S. acknowledge support from the U.S. Army Research Office (ARO) through Grant No. W911NF-22-2-0117 and the U.S. Army Contract No. W911NF-25-1-0112. Portions of this research were conducted with the advanced computing resources provided by Texas A&M High Performance Research Computing. The calculations reported in this paper were partially performed at TUBITAK ULAKBIM, High Performance and Grid Computing Center (TRUBA resources).

# References
