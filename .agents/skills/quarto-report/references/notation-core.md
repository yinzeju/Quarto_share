## Basic typography
- Vectors: bold lowercase upright, e.g. $\mathbf{x},\mathbf{a}$
- Matrices: bold uppercase upright, e.g. $\mathbf{A}$
- Tensors: Euler script, e.g. $\boldsymbol{\mathsf{T}},\boldsymbol{\mathsf{W}}$
- Transpose: $\mathbf{A}^\top$
- Complex conjugate: $\overline{\mathbf{A}}$
- Conjugate transpose: $\mathbf{A}^*$
- Pseudo-inverse: $\mathbf{A}^\dagger$
## Mathematical object types
- Scalar field: $\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}$
- Functions: $f,g,h,\varphi,\psi$
- Functionals: $F,G$
- Operators: $\mathcal{A},\mathcal{K},\mathcal{L},\mathcal{P}$
- Function / observable spaces: $\mathcal{H},\mathcal{G}$
- Continuous dual space: $\mathcal{H}^\star$
## Basic space notation
- Identity operator: $\mathcal{I}$
- Finite-dimensional subspace: $\mathcal{V}_N=\operatorname{span}\{\psi_1,\ldots,\psi_N\}$
- Orthogonal projection: $\mathcal{P}_N:\mathcal{H}\to\mathcal{V}_N$
- Complementary projection: $\mathcal{Q}_N:=\mathcal{I}-\mathcal{P}_N$
- Domain of an operator: $D(\mathcal{A})$
- Projection residual: Default closure / out-of-subspace residual: for $g\in D(\mathcal{A})$, define $\eta_N(g;\mathcal{A}):=(\mathcal{I}-\mathcal{P}_N)\mathcal{A}g=\mathcal{Q}_N\mathcal{A}g$
- Space norm: $\|g\|_{\mathcal{H}}$
- Operator norm: $\|\mathcal{A}\|_{\mathrm {op}}$
## Pairing and adjoint notions
- Dual pairing: $\langle F,g\rangle_{\mathcal{H}^\star,\mathcal{H}}:=F(g)$, $F\in\mathcal{H}^\star$, $g\in\mathcal{H}$
- Dual operator: $\mathcal{A}^\star:\mathcal{H}^\star\to\mathcal{H}^\star$, $\langle\mathcal{A}^\star F,g\rangle_{\mathcal{H}^\star,\mathcal{H}}=\langle F,\mathcal{A}g\rangle_{\mathcal{H}^\star,\mathcal{H}}$
- Adjoint operator: $\mathcal{A}^*:\mathcal{H}\to\mathcal{H}$, $\langle\mathcal{A}g,h\rangle_\mu=\langle g,\mathcal{A}^*h\rangle_\mu$
- Inner product in Hilbert settings: $\langle g,h\rangle_\mu:=\int_{\mathcal{X}}g(\mathbf{x})\overline{h(\mathbf{x})}\,\mathrm{d}\mu(\mathbf{x})$
## Spectral notation
- Eigenspace: $\mathcal{E}_\lambda(\mathcal{A}):=\ker(\lambda\mathcal{I}-\mathcal{A})$
- Resolvent: $\mathcal{R}(z,\mathcal{A}):=(z\mathcal{I}-\mathcal{A})^{-1}$, $z\in\rho(\mathcal{A})$
- Point / continuous / residual spectrum: $\sigma_p(\mathcal{A}),\sigma_c(\mathcal{A}),\sigma_r(\mathcal{A})$
- Pseudospectrum: $\sigma_\varepsilon(\mathcal{A}):=\{z\in\mathbb{C}:\|\mathcal{R}(z,\mathcal{A})\|>\varepsilon^{-1}\}$, $\varepsilon>0$
## Differential notation
- Time derivative: $\dot{x}:=\frac{\mathrm d x}{\mathrm dt}$, $\dot{\mathbf{x}}:=\frac{\mathrm d\mathbf{x}}{\mathrm dt}$, $\dot{\mathbf A}:=\frac{\mathrm d\mathbf A}{\mathrm dt}$
- Scalar partial derivative: $\partial_{x_j}f:=\frac{\partial f}{\partial x_j}$, $\partial_t f:=\frac{\partial f}{\partial t}$
- Derivative / Jacobian of a map: $D\mathbf f(\mathbf x)$; with specified variable, $D_{\mathbf x}\mathbf f$
- Directional action: $D\mathbf f(\mathbf x)[\mathbf h]$
- Scalar gradient: $\nabla f(\mathbf x)$, with $Df(\mathbf x)[\mathbf h]=\nabla f(\mathbf x)^\top\mathbf h$
- Matrix-valued map: for $\mathbf A:\mathbb R^n\to\mathbb K^{p\times q}$, use $D\mathbf A(\mathbf x)[\mathbf h]\in\mathbb K^{p\times q}$
- Second derivative: $D^2f(\mathbf x)[\mathbf h_1,\mathbf h_2]$; scalar Hessian: $\nabla^2f(\mathbf x)$
- Functional derivative: for $F:\mathcal H\to\mathbb R$, use $DF(g)\in\mathcal H^\star$ and $DF(g)[h]$
## Reference and Perturbation Notation
- Reference-point subscript: $\star$ denotes an object tied to a specified reference point, e.g. $\mathbf{x}_\star,\mathbf{A}_\star$; distinguish it from adjoint $^{*}$ and dual $^{\star}$.
- Perturbation / first variation: $\delta\mathbf{x}$; finite increment / algorithmic correction: $\Delta\mathbf{x}$. Their precise meanings are specified locally.
- Column concatenation: $\operatorname{col}(\mathbf{a},\mathbf{b}):=[\mathbf{a}^\top,\mathbf{b}^\top]^\top$.
- Identity matrix: $\mathbf{I}$ or $\mathbf{I}_d$; identity operator: $\mathcal{I}$.
- Zero vector / matrix: $\mathbf{0}$, with dimension determined by context.
- Full state dimension: $d_x:=\dim\mathcal{X}$ in finite-dimensional settings.
- Spectral / mechanical modal index: $j$, distinguished from temporal snapshot index $m$ and dictionary basis index $n$.
## Generic indices
- $m$: temporal snapshot index
- $n$: basis / feature index
- $d$: local physical dimension per spatial point
- $M$: total number of samples / snapshots
- $N$: subspace dimension / dictionary size
- $N_x$: number of spatial discretization points
