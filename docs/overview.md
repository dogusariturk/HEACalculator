# Overview

## High Entropy Alloys

High Entropy Alloys (HEAs) are a class of metallic materials composed of five or more principal elements in near-equimolar ratios (typically 5–35 at% each). Unlike conventional alloys that center on one or two base metals, HEAs exploit the configurational entropy of mixing to stabilize single-phase disordered solid solutions over intermetallic compounds, often yielding exceptional combinations of mechanical strength, hardness, and corrosion resistance.

Predicting whether a given multi-component composition will form a solid solution (rather than segregate into intermetallic phases) is a central challenge in HEA design. `HEACalculator` implements a suite of published phenomenological criteria that use thermodynamic and structural parameters as proxies for phase stability.

---

## Calculated Parameters

### Mixing Enthalpy

$$
\Delta H_{\text{mix}} = \sum_{i<j} 4\,\Delta H_{ij}^{\text{mix}}\,x_i x_j \quad [\text{kJ/mol}]
$$

where the sum runs over each unique pair of elements once, $x_i$ is the mole fraction of element $i$, and $\Delta H_{ij}^{\text{mix}}$ is the binary mixing enthalpy of elements $i$ and $j$ from Miedema's model, as tabulated by Takeuchi and Inoue.[^18] The formula follows Zhang *et al.*[^1]

### Miedema Mixing Enthalpy

$$
\Delta H_{\text{mix}}^{\text{Miedema}} = \sum_{i \neq j} x_i x_j
\bigl(x_j H_{\text{chem},ij} + x_i H_{\text{chem},ji}
+ x_j H_{\text{el},ij} + x_i H_{\text{el},ji}
+ x_j H_{\text{struct},ij} + x_i H_{\text{struct},ji}\bigr)
\quad [\text{kJ/mol}]
$$

where the three contributions for each ordered pair $(i \to j)$ are:

- **Chemical interface term** $H_{\text{chem}}$: from the Miedema macroscopic atom model (de Boer *et al.* 1988)[^14]
- **Elastic mismatch term** $H_{\text{el}}$: from Eshelby theory applied to atomic size and bulk/shear modulus mismatches
- **Structural term** $H_{\text{struct}}$: from Niessen and Miedema (1983)[^15] via tabulated valence-dependent energies

This three-term formula follows King *et al.* Supplementary Eq. S8.[^11] It is used for the Model 8 solid-solution criterion.

### Mixing Entropy

$$
\Delta S_{\text{mix}} = -R \sum_{i=1}^{n} x_i \ln x_i \quad [\text{J/K·mol}]
$$

where $R = 8.314\,\text{J/(mol·K)}$ is the gas constant.

### Formation Enthalpy

$$
\Delta H_f = \sum_{i<j} 4\,\Delta H_{ij}^f\,x_i x_j \quad [\text{meV/atom}]
$$

Binary formation enthalpies $\Delta H_{ij}^f$ are taken from DFT calculations by Troparevsky *et al.*[^2]

### Atomic Size Difference (δ) { data-toc-label="Atomic Size Difference" }

$$
\delta = \sqrt{\sum_{i=1}^{n} x_i \left(1 - \frac{r_i}{\bar{r}}\right)^2} \times 100 \quad [\%]
$$

where $r_i$ is the atomic radius of element $i$ and $\bar{r} = \sum_i x_i r_i$ is the average radius.[^4][^21]

### Allen Electronegativity Difference ($\Delta\chi_{\text{Allen}}$) { data-toc-label="Allen Electronegativity Difference" }

$$
\Delta\chi_{\text{Allen}} = \sqrt{\sum_{i=1}^{n} x_i \left(1 - \frac{\chi_i}{\bar{\chi}}\right)^2} \times 100 \quad [\%]
$$

where $\chi_i$ is the Allen configuration energy (CE) of element $i$ in Pauling units and $\bar{\chi} = \sum_i x_i \chi_i$ is the composition-weighted average.[^12][^13]

### Pauling Electronegativity Difference ($\Delta\chi_{\text{Pauling}}$) { data-toc-label="Pauling Electronegativity Difference" }

$$
\Delta\chi_{\text{Pauling}} = \sqrt{\sum_{i=1}^{n} x_i \left(1 - \frac{\chi_i}{\bar{\chi}}\right)^2} \times 100 \quad [\%]
$$

where $\chi_i$ is the Pauling electronegativity of element $i$ and $\bar{\chi} = \sum_i x_i \chi_i$ is the composition-weighted average.[^16]

### Omega (Ω) { data-toc-label="Omega" }

$$
\Omega = \frac{T_m \,\Delta S_{\text{mix}}}{|\Delta H_{\text{mix}}|}
$$

where $T_m = \sum_i x_i T_{m,i}$ is the composition-weighted melting temperature.[^5]

### Gamma (γ) { data-toc-label="Gamma" }

$$
\gamma = \omega_S / \omega_L
= \left(1 - \sqrt{\frac{(r_S + \bar{r})^2 - \bar{r}^2}{(r_S + \bar{r})^2}}\right)
\Bigg/
\left(1 - \sqrt{\frac{(r_L + \bar{r})^2 - \bar{r}^2}{(r_L + \bar{r})^2}}\right)
$$

where $\omega_S$ and $\omega_L$ are the solid angles of the smallest and largest atoms, $r_S$ and $r_L$ are their radii, and $\bar{r}$ is the average radius.[^6]

### Lambda (λ) { data-toc-label="Lambda" }

$$
\lambda = \frac{\Delta S_{\text{mix}}}{\delta^2}
$$

A combined entropy–misfit parameter.[^7]

### Valence Electron Concentration (VEC)

$$
\text{VEC} = \sum_{i=1}^{n} x_i\,(\text{VEC})_i
$$

Used to predict the stable crystal structure (FCC, BCC, or HCP).[^3]

### Hume-Rothery Electron-to-Atom Ratio (e/a)

$$
e/a = \sum_{i=1}^{n} x_i\,(e/a)_i
$$

where $(e/a)_i$ is the number of outer s+p electrons of element $i$; d and f electrons are not counted. This follows the Hume-Rothery convention and is distinct from VEC.[^17]

### Density

$$
\rho = \frac{\sum_i x_i M_i}{\sum_i x_i V_i} \quad [\text{g/cm}^3]
$$

where $M_i$ and $V_i$ are the molar mass and atomic volume of element $i$.

### Melting Temperature

$$
\overline{T}_m = \sum_{i=1}^{n} x_i\,T_{m,i} \quad [\text{K}]
$$

---

## Solid-Solution Prediction Models

`HEACalculator` implements eight published criteria. Each model returns `"Solid Solution"`, `"Intermetallic"`, or `"Multiple Phases"`. A model returns `"N/A"` when the data it requires are unavailable.

| Model | Author(s)                   | Criteria                                                                                                                                 | Reference                                                                    |
|-------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 1     | Yang & Zhang (2012)         | $\Omega \geq 1.1$ and $\delta \leq 6.6\%$                                                                                                | [5](#fn:5)                                                                   |
| 2     | Guo *et al.* (2013)         | $-11.6 < \Delta H_{\text{mix}} < 3.2\,\text{kJ/mol}$ and $\delta < 6.6\%$                                                                | [8](#fn:8){ #fnref:8 }                                                       |
| 3     | Wang *et al.* (2015)        | $\gamma < 1.175$                                                                                                                         | [6](#fn:6)                                                                   |
| 4     | Singh *et al.* (2014)       | $\lambda > 0.96$ (SS); $0.24 \leq \lambda \leq 0.96$ (SS + compound); $\lambda < 0.24$ (compound)                                        | [7](#fn:7)                                                                   |
| 5     | Ye *et al.* (2015)          | $\phi = (S_C - S_H) / \lvert S_E\rvert \geq 20$                                                                                          | [9](#fn:9){ #fnref:9 }, [19](#fn:19){ #fnref:19 }, [20](#fn:20){ #fnref:20 } |
| 6     | Troparevsky *et al.* (2015) | $\Delta H_f^{\min} > -T_{\text{crit}}\Delta S_{\text{mix}}$ and $\Delta H_f^{\max} < 37\,\text{meV/atom}$, $T_{\text{crit}} = 0.55\,T_m$ | [2](#fn:2)                                                                   |
| 7     | Senkov & Miracle (2016)     | $k_1 = \Delta H_f / \Delta H_{\text{mix}} < 1 + \Omega(T_{\text{anneal}})(1 - k_2)$, $T_{\text{anneal}} = 0.55\,T_m$, $k_2 = 0.6$        | [10](#fn:10){ #fnref:10 }                                                    |
| 8     | King *et al.* (2016)        | $\phi = \Delta G_{\text{SS}} / (-\lvert \Delta G_{\max}\rvert) \geq 1$                                                                   | [11](#fn:11)                                                                 |

A microstructure prediction based on VEC is also provided. The HCP window is tested first, so a composition falling in it is reported as HCP even though it also satisfies the BCC bound:

- 2.5 ≤ VEC ≤ 3.5: HCP
- VEC ≥ 8: FCC
- VEC ≤ 6.87: BCC
- 6.87 < VEC < 8: BCC + FCC (mixed)

---

## References

[^1]: Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. *Prog. Mater. Sci.* **2014**, *61*, 1–93.
[^2]: Troparevsky, M.C.; Morris, J.R.; Kent, P.R.C.; Lupini, A.R.; Stocks, G.M. *Phys. Rev. X* **2015**, *5*(1), 011041.
[^3]: Guo, S.; Ng, C.; Lu, J.; Liu, C.T. *J. Appl. Phys.* **2011**, *109*, 103505.
[^4]: Fang, S.S.; Xiao, X.S.; Xia, L.; Li, W.H.; Dong, Y.D. *J. Non-Cryst. Solids* **2003**, *321*, 120–125.
[^5]: Yang, X.; Zhang, Y. *Mater. Chem. Phys.* **2012**, *132*, 233–238.
[^6]: Wang, Z.; Huang, Y.; Yang, Y.; Wang, J.; Liu, C.T. *Scr. Mater.* **2015**, *94*, 28–31.
[^7]: Singh, A.K.; Kumar, N.; Dwivedi, A.; Subramaniam, A. *Intermetallics* **2014**, *53*, 112–119.
[^8]: Guo, S.; Hu, Q.; Ng, C.; Liu, C.T. *Intermetallics* **2013**, *41*, 96–103.
[^9]: Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. *Scr. Mater.* **2015**, *104*, 53–55.
[^10]: Senkov, O.N.; Miracle, D.B. *J. Alloys Compd.* **2016**, *658*, 603–607.
[^11]: King, D.J.M.; Middleburgh, S.C.; McGregor, A.G.; Cortie, M.B. *Acta Mater.* **2016**, *104*, 172–179.
[^12]: Mann, J.B.; Meek, T.L.; Allen, L.C. *J. Am. Chem. Soc.* **2000**, *122*, 2780–2783.
[^13]: Mann, J.B.; Meek, T.L.; Knight, E.T.; Capitani, J.F.; Allen, L.C. *J. Am. Chem. Soc.* **2000**, *122*, 5132–5137.
[^14]: de Boer, F.R.; Boom, R.; Mattens, W.C.M.; Miedema, A.R.; Niessen, A.K. *Cohesion in Metals: Transition Metal Alloys.* North-Holland, Amsterdam, 1988.
[^15]: Niessen, A.K.; Miedema, A.R. *Ber. Bunsenges. Phys. Chem.* **1983**, *87*, 717–725.
[^16]: Haynes, W.M. *CRC Handbook of Chemistry and Physics*, 95th ed.; CRC Press: Boca Raton, FL, 2014. ISBN 9781482208689.
[^17]: Hume-Rothery, W.; Smallman, R.E.; Haworth, C.W. *The Structure of Metals and Alloys*, 5th ed.; Institute of Metals: London, 1969.
[^18]: Takeuchi, A.; Inoue, A. *Mater. Trans.* **2005**, *46*(12), 2817–2829.
[^19]: Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. *Intermetallics* **2015**, *59*, 75–80.
[^20]: Mansoori, G.A.; Carnahan, N.F.; Starling, K.E.; Leland, T.W., Jr. *J. Chem. Phys.* **1971**, *54*, 1523–1525.
[^21]: Senkov, O.N.; Miracle, D.B. *Mater. Res. Bull.* **2001**, *36*, 2183–2198.
