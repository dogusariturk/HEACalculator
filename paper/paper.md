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

Those papers list nearly 500 compositions between them. All eight criteria give an answer for 70% of them, but they rarely agree. Where they disagree, nearly three in four split three ways, calling the same alloy a solid solution, an intermetallic, and multiple phases. AlCoCrFeNi is typical, with two criteria reporting a solid solution, two an intermetallic, and four multiple phases. Which criterion a study picks therefore usually determines the answer it reports. No criterion has emerged as the most reliable, so there is no good reason to report one and drop the others.

| **Model** | **Solid-solution criterion** | **Reference** |
|:------|:---------------------------------------------|:---------------|
| 1 | $\Omega \geq 1.1$ and $\delta_\text{CN12} \leq 6.6\%$ | [@yang2012] |
| 2 | $-11.6 < \Delta H_\text{mix} < 3.2$ kJ/mol and $\delta < 6.6\%$ | [@guo2013] |
| 3 | $\gamma < 1.175$ | [@wang2015] |
| 4 | $\Lambda > 0.96$; intermetallic if $\Lambda < 0.24$, otherwise multiple phases | [@singh2014] |
| 5 | $\phi \geq 20$ | [@ye2015scr] |
| 6 | $\min(\Delta H_{ij}^f) > -T_\text{crit}\Delta S_\text{mix}$ and $\max(\Delta H_{ij}^f) < 37$ meV/atom | [@troparevsky2015] |
| 7 | $\Delta H_f/\Delta H_\text{mix} < \Omega(T_\text{ann})(1-k_2)+1$ | [@senkov2016] |
| 8 | $\varPhi = \Delta G_{SS}/(-\lvert\Delta G_\text{max}\rvert) \geq 1$ | [@king2016] |

: Published solid-solution criteria implemented in `HEACalculator`. Descriptor definitions, radius sets, and default parameters are given in the [documentation](https://dogusariturk.github.io/HEACalculator/overview/). \label{tab:models}

`HEACalculator` computes sixteen descriptors and implements all eight published criteria (\autoref{tab:models}), plus the VEC-based crystal-structure rule of @guo2011, in one validated, reusable package. It bundles a database of 118 elements with atomic radii from @guoliu2011 and @kittel2005, 2,628 binary mixing enthalpies from @takeuchi2005, and 435 binary formation enthalpies derived from density functional theory (DFT) data from @troparevsky2015, along with utilities for single-composition analysis, parameter sweeps, and batch processing. It is aimed at materials scientists screening candidate compositions for alloy design or experiments.


# State of the Field

The closest interactive peer is `HEAPS` [@martin2022heaps], an open-source (CC0) MATLAB program that computes a larger set of semi-empirical descriptors and criteria, including mechanical-property heuristics, and screens candidate alloys against user-defined constraints. Its installer targets 64-bit Windows with the MATLAB Runtime, and running its source requires a MATLAB license. `HEACalculator` covers a narrower set of solid-solution descriptors but packages them as a cross-platform Python library with an API, CLI, and optional GUI, so other projects can depend on and test the calculations without proprietary software.

`matminer` [@ward2018matminer] provides composition descriptors, including alloy-specific featurizers, and leaves phase prediction to downstream models. Two HEA tools build such models: `AutomaticFeaturizerMPEA` [@subedi2022], a Jupyter notebook whose accompanying study trains a neural network on `matminer` features to detect intermetallic phases, and `pyMPEALab` [@subedi2022pympealab], a neural-network phase classifier with a graphical interface. Both return a learned prediction, whereas `HEACalculator` reports the verdict of each published criterion, so a user can see which rules a composition passes and which it fails.

The closest peer in library form is `hea-bench` [@fieser2026heabench], first released in 2026, seven years after `HEACalculator` was made public. It computes a similar descriptor set, applies nine empirical phase rules [@fieser2026heabenchsw], and extends both to high-entropy oxides. It works from a single radius tabulation, while `HEACalculator` carries two and gives each criterion the tabulation that reproduces its source paper's published size parameters. The published thresholds were calibrated on particular radius sets and do not transfer between them. `hea-bench` has since added `HEACalculator` as an optional backend, as described in the Research Impact Statement.

Model-specific scripts and spreadsheets in supplementary material reproduce particular results but are not built as dependencies, and contributing to existing interactive tools would not supply that programmatic capability. `HEACalculator` is versioned and tested, so other work can cite a specific release and build on it.

# Software Design

`HEACalculator` is organized around a shared calculation core rather than around its user interfaces. A common parser normalizes compositions from the CLI, GUI, or Python API into one internal representation, which accepts compact formulas, explicit stoichiometries, and nested notation. The thermodynamic engine reads only that representation, so a composition gives the same result through any of the three interfaces. A separate prediction layer then applies the published thresholds to that one descriptor set.

The reference data ships as JSON inside the package, and the data modules cite the published sources they draw on. When a required pair is missing, the data layer raises a typed exception rather than substituting a value. The calculation layer turns that into an `N/A` for the affected descriptor. Incomplete coverage stays visible, and users can tell an unsupported composition from a physically meaningful negative result.

![The `HEACalculator` graphical interface showing the HEA Parameters page. Users select elements from the periodic table, assign atomic-percent compositions, and calculate thermodynamic descriptors and solid-solution predictions in a single shared results view.\label{fig:gui}](figure_1.png)

Model 8 does not use the tabulated pair enthalpies. Its Gibbs energies follow the supplementary equations of @king2016, using the Miedema model [@deboer1988; @niessen1983] with parameters for 35 elements, so it reports `N/A` for compositions outside that set.

The test suite checks every model against the data of the paper that introduced it, nearly 500 compositions in all. The descriptors reproduce the published values closely, and the criteria return the published phase label for roughly nine alloys in ten.

The CLI screens composition ranges in parallel across CPU cores and reads candidate alloys from CSV files, and the optional PyQt6 desktop application covers interactive use (\autoref{fig:gui}).

# Research Impact Statement

`HEACalculator` has also been used as a descriptor source rather than as a phase-screening tool, supplying domain-specific features alongside general-purpose composition databases such as JARVIS [@choudhary2018jarvis; @choudhary2020jarvis], Oliynyk [@oliynyk2016], Magpie [@ward2016magpie], and mat2vec [@tshitoyan2019mat2vec]. Hossein @zadeh2024 combined those sources into 4937 candidate features and fitted an interpretable piecewise linear regression for the $\lambda_2$ compatibility parameter between the austenite and martensite phases of NiTi shape memory alloys, a quantity that correlates with transformation hysteresis. @sheikh2025 assembled 3372 features for Vickers hardness in refractory high-entropy alloys and narrowed them to six predictors through recursive feature elimination and mutual-information filtering. In each case the package supplied composition descriptors for a target property it does not itself predict, which is the reuse a packaged calculation core is meant to support.

`HEACalculator` has been publicly available since 2019. `hea-bench` [@fieser2026heabenchsw], an independent calculator for HEAs and high-entropy oxides, uses it as an optional backend through an adapter that maps fifteen `HEACalculator` descriptors, seven of which `hea-bench` does not compute itself, and its documentation compares the two backends on the shared ones. Quantities such as the King Gibbs energies, the Ye $\phi$, and the excess entropy are left unmapped because the packages compute them differently. This is the ambiguity described in the Statement of Need, reached independently by a group trying to make the two packages interoperate.

# AI Usage Disclosure

Claude Code (Anthropic, Claude Opus 5) and Codex (OpenAI, GPT-5) were used in the development of `HEACalculator` to draft docstrings and documentation, scaffold unit tests, and suggest refactorings of existing code, and to copy-edit this manuscript. The authors reviewed, edited, and validated all AI-assisted output before including it, accepting suggested code changes only after the full test suite passed, and are responsible for the correctness of the software, its documentation, and this paper.

# Acknowledgements

R.A. and D.S. acknowledge support from the U.S. Army Research Office (ARO) through Grant No. W911NF-22-2-0117 and the U.S. Army Contract No. W911NF-25-1-0112. Portions of this research were conducted with the advanced computing resources provided by Texas A&M High Performance Research Computing. The calculations reported in this paper were partially performed at TUBITAK ULAKBIM, High Performance and Grid Computing Center (TRUBA resources).

# References
