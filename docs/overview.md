# Overview

## High Entropy Alloys

High Entropy Alloys (HEAs) are a class of metallic materials composed of five or more principal elements in near-equimolar ratios (typically 5–35 at% each). Unlike conventional alloys that center on one or two base metals, HEAs exploit the configurational entropy of mixing to stabilize single-phase disordered solid solutions over intermetallic compounds, often yielding exceptional combinations of mechanical strength, hardness, and corrosion resistance.

Predicting whether a given multi-component composition will form a solid solution (rather than segregate into intermetallic phases) is a central challenge in HEA design. `HEACalculator` implements a suite of published phenomenological criteria that use thermodynamic and structural parameters as proxies for phase stability.

---

## Calculated Parameters

### Mixing Enthalpy

$$
\Delta H_{\text{mix}} = \sum_{i=1,\,i\neq j}^{n} 4\,\Delta H_{AB}^{\text{mix}}\,x_i x_j \quad [\text{kJ/mol}]
$$

where $x_i$ is the mole fraction of element $i$ and $\Delta H_{AB}^{\text{mix}}$ is the binary mixing enthalpy from Miedema's model.[^1]

### Mixing Entropy

$$
\Delta S_{\text{mix}} = -R \sum_{i=1}^{n} x_i \ln x_i \quad [\text{J/K·mol}]
$$

where $R = 8.314\,\text{J/(mol·K)}$ is the gas constant.

### Formation Enthalpy

$$
\Delta H_f = \sum_{i=1,\,i\neq j}^{n} x_i x_j\,\Delta H_{ij}^f \quad [\text{meV/atom}]
$$

Binary formation enthalpies $\Delta H_{ij}^f$ are taken from DFT calculations by Troparevsky *et al.*[^2]

### Atomic Size Difference (δ) { data-toc-label="Atomic Size Difference" }

$$
\delta = \sqrt{\sum_{i=1}^{n} x_i \left(1 - \frac{r_i}{\bar{r}}\right)^2} \times 100 \quad [\%]
$$

where $r_i$ is the atomic radius of element $i$ and $\bar{r} = \sum_i x_i r_i$ is the average radius.[^4]

### Electronegativity Difference ($\Delta\chi_{\text{Allen}}$) { data-toc-label="Electronegativity Difference" }

$$
\Delta\chi_{\text{Allen}} = \sqrt{\sum_{i=1}^{n} x_i \left(1 - \frac{\chi_i}{\bar{\chi}}\right)^2} \times 100 \quad [\%]
$$

where $\chi_i$ is the Allen configuration energy (CE) of element $i$ in Pauling units and $\bar{\chi} = \sum_i x_i \chi_i$ is the composition-weighted average.[^12][^13]

### Omega (Ω) { data-toc-label="Omega" }

$$
\Omega = \frac{T_m \,\Delta S_{\text{mix}}}{|\Delta H_{\text{mix}}|}
$$

where $T_m = \sum_i x_i T_{m,i}$ is the composition-weighted melting temperature.[^5]

### Gamma (γ) { data-toc-label="Gamma" }

$$
\gamma = \frac{1 - \sqrt{1 - \left(\frac{r_S}{r_S + \bar{r}}\right)^2}}{1 - \sqrt{1 - \left(\frac{r_L}{r_L + \bar{r}}\right)^2}}
$$

where $r_S$ and $r_L$ are the radii of the smallest and largest atoms, respectively.[^6]

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

### Density

$$
\rho = \frac{\sum_i x_i M_i}{\sum_i x_i V_i} \quad [\text{g/cm}^3]
$$

where $M_i$ and $V_i$ are the molar mass and atomic volume of element $i$.

### Melting Temperature

$$
T_m = \sum_{i=1}^{n} x_i\,T_{m,i} \quad [\text{K}]
$$

---

## Solid-Solution Prediction Models

`HEACalculator` implements eight published criteria. Each model returns `"Solid Solution"`, `"Intermetallic"`, or `"Multiple Phases"`.

| Model | Author(s)                   | Criteria                                                                                          | Reference    |
|-------|-----------------------------|---------------------------------------------------------------------------------------------------|--------------|
| 1     | Yang & Zhang (2012)         | $\Omega \geq 1.1$ and $\delta \leq 6.6\%$                                                         | [5](#fn:5)   |
| 2     | Guo *et al.* (2013)         | $-11.6 < \Delta H_{\text{mix}} < 3.2\,\text{kJ/mol}$ and $\delta < 6.6\%$                         | [8](#fn:8)   |
| 3     | Wang *et al.* (2015)        | $\Omega \geq 1.1$ and $\gamma < 1.175$                                                            | [6](#fn:6)   |
| 4     | Singh *et al.* (2014)       | $\lambda > 0.96$ (SS); $0.24 \leq \lambda \leq 0.96$ (SS + compound); $\lambda < 0.24$ (compound) | [7](#fn:7)   |
| 5     | Ye *et al.* (2015)          | $\phi = \Omega - 1 \geq 20$                                                                       | [9](#fn:9)   |
| 6     | Troparevsky *et al.* (2015) | All binary $\Delta H_f$ within $\pm k_B T$ window at $0.55\,T_m$                                  | [2](#fn:2)   |
| 7     | Senkov & Miracle (2016)     | $\Omega(T_{\text{anneal}}) \geq k_2 \cdot \Delta S_{\text{mix}} / R$                              | [10](#fn:10) |
| 8     | King *et al.* (2016)        | $\phi = \Delta G_{\text{SS}} / (-\lvert \Delta G_{\max}\rvert) \geq 1$                            | [11](#fn:11) |

A microstructure prediction based on VEC is also provided:

- VEC ≥ 8: FCC
- VEC < 6.87: BCC
- 6.87 ≤ VEC < 8: BCC + FCC (mixed)
- VEC < 5 and certain conditions: HCP

---

## References

[^1]: Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P.K.; Lu, Z.P. *Prog. Mater. Sci.* **2014**, *61*, 1–93.
[^2]: Troparevsky, M. C.; Morris, J. R.; Kent, P. R. C.; Lupini, A. R.; Stocks, G. M. *Phys. Rev. X* **2015**, *5*(1), 011041.
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
