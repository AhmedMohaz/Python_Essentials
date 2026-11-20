"""BIT 2118 Scientific Computing: consolidated Tasks 1–20.

Run:
    python scientific_computing_tasks_1_20.py

The script prints representative results and writes plots to ./graphs.
Dependencies: numpy, scipy, matplotlib
"""
from __future__ import annotations

from pathlib import Path
from time import perf_counter
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, simpson
from scipy.interpolate import CubicSpline, interp1d
from scipy.optimize import curve_fit, minimize, root, root_scalar
from scipy.linalg import lu_factor, lu_solve

ROOT = Path(__file__).resolve().parent
GRAPH_DIR = ROOT / "graphs"
GRAPH_DIR.mkdir(exist_ok=True)


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(GRAPH_DIR / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


# ================================ TASK 01 ================================
# NumPy arrays: hourly temperature statistics and unit conversion.
def task_01_numpy_temperature() -> dict:
    c = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
                  25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
                  26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
    f = 1.8 * c + 32
    changed = c.copy(); changed[12] = 35.0
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(np.arange(24), c, "o-", label="Temperature (°C)")
    ax.plot(np.arange(24), changed, "s--", label="Changed peak")
    ax.set(title="Task 1: Hourly Temperature", xlabel="Hour", ylabel="°C")
    ax.grid(True); ax.legend(); save(fig, "task_01_temperature.png")
    return {"mean_c": c.mean(), "min_c": c.min(), "max_c": c.max(),
            "changed_mean_c": changed.mean(), "fahrenheit": f}


# ================================ TASK 02 ================================
# Vectorized mathematical functions and loop benchmarking.
def task_02_vectorization() -> dict:
    rng = np.random.default_rng(42)
    latency_ms = rng.uniform(5, 250, 1_000_000)
    t0 = perf_counter(); loop_result = [(x / 1000.0) ** 2 for x in latency_ms]; loop_s = perf_counter() - t0
    t0 = perf_counter(); vector_result = (latency_ms / 1000.0) ** 2; vector_s = perf_counter() - t0
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(["Python loop", "NumPy vectorized"], [loop_s, vector_s], color=["#d95f02", "#1b9e77"])
    ax.set(title="Task 2: Loop versus Vectorized Runtime", ylabel="Seconds (one run)")
    ax.grid(axis="y"); save(fig, "task_02_vectorization.png")
    return {"loop_seconds": loop_s, "vectorized_seconds": vector_s,
            "speedup": loop_s / max(vector_s, 1e-12), "mean_squared_seconds": float(np.mean(vector_result))}


# ================================ TASK 03 ================================
# Floating-point arithmetic and numerical errors.
def task_03_floating_point() -> dict:
    calculated, expected = 0.1 + 0.2, 0.3
    true_value, approx = np.sqrt(2), 1.414
    abs_error = abs(true_value - approx)
    rel_error = abs_error / abs(true_value)
    return {"calculated": calculated, "exact_equal": calculated == expected,
            "close": bool(np.isclose(calculated, expected)), "absolute_error": abs_error,
            "relative_error": rel_error}


# ================================ TASK 04 ================================
# Matrix algebra: rotation, scaling, determinant, and transformed points.
def task_04_matrix_transform() -> dict:
    points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    angle = np.deg2rad(45)
    rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    scale = np.diag([2.0, 1.5])
    transform = rotation @ scale
    transformed = points @ transform.T
    fig, ax = plt.subplots(figsize=(6, 6))
    closed = np.vstack([points, points[0]]); new_closed = np.vstack([transformed, transformed[0]])
    ax.plot(closed[:, 0], closed[:, 1], "o--", label="Original")
    ax.plot(new_closed[:, 0], new_closed[:, 1], "o-", label="Transformed")
    ax.axhline(0, color="gray", lw=.6); ax.axvline(0, color="gray", lw=.6)
    ax.set(title="Task 4: Rotation and Scaling", xlabel="x", ylabel="y", aspect="equal")
    ax.grid(True); ax.legend(); save(fig, "task_04_matrix_transform.png")
    return {"transformation": transform, "points": transformed, "determinant": np.linalg.det(transform)}


# ================================ TASK 05 ================================
# Quadratic curve fitting and approximation.
def task_05_curve_fit() -> dict:
    x = np.array([50, 100, 150, 200, 250, 300, 350.], float)
    y = np.array([82, 95, 115, 145, 185, 238, 305.], float)
    model = lambda x, a, b, c: a*x*x + b*x + c
    params, _ = curve_fit(model, x, y)
    pred = model(x, *params); rmse = np.sqrt(np.mean((y - pred) ** 2))
    xp = np.linspace(50, 450, 300)
    fig, ax = plt.subplots(figsize=(8, 4.5)); ax.scatter(x, y, label="Measurements")
    ax.plot(xp, model(xp, *params), label="Quadratic fit")
    ax.scatter([400], [model(400, *params)], marker="x", s=80, label="Prediction at 400")
    ax.set(title="Task 5: Server Response-Time Curve Fit", xlabel="Concurrent users", ylabel="Response time (ms)")
    ax.grid(True); ax.legend(); save(fig, "task_05_curve_fit.png")
    return {"parameters": params, "rmse_ms": rmse, "prediction_400_ms": model(400, *params)}


# ================================ TASK 06 ================================
# Direct solution of a linear system / power-grid allocation.
def task_06_linear_system() -> dict:
    A = np.array([[4., 2.], [8., 12.]])
    b = np.array([20., 72.]); x = np.linalg.solve(A, b)
    b_changed = np.array([20., 96.]); x_changed = np.linalg.solve(A, b_changed)
    return {"solution": x, "changed_solution": x_changed, "residual_norm": np.linalg.norm(b - A @ x)}


# ================================ TASK 07 ================================
# LU factorization for repeated structural-load solves.
def task_07_lu_decomposition() -> dict:
    A = np.array([[4., 1., 0.], [-1., 4., -1.], [0., -1., 3.]])
    loads = [np.array(v, float) for v in ([15, 10, 10], [16, 11, 9], [14, 12, 11])]
    lu, piv = lu_factor(A); solutions = [lu_solve((lu, piv), b) for b in loads]
    return {"solutions": solutions, "residuals": [np.linalg.norm(A @ x - b) for x, b in zip(solutions, loads)]}


# ================================ TASK 08 ================================
# Jacobi and Gauss–Seidel iterative methods.
def task_08_iterative_methods() -> dict:
    A = np.array([[2., -1, 0, 0, 0], [-1, 2., -1, 0, 0], [0, -1, 2., -1, 0], [0, 0, -1, 2., -1], [0, 0, 0, -1, 2.]])
    b = np.array([100., 0, 0, 0, 20.]); D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros(5); ej = []
    for _ in range(500):
        xn = (b - R @ x) / D; ej.append(np.max(abs(xn - x))); x = xn
        if ej[-1] < 1e-8: break
    xg = np.zeros(5); eg = []
    for _ in range(500):
        old = xg.copy()
        for i in range(5): xg[i] = (b[i] - A[i, :i] @ xg[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        eg.append(np.max(abs(xg - old)))
        if eg[-1] < 1e-8: break
    fig, ax = plt.subplots(figsize=(8, 4.5)); ax.semilogy(ej, label="Jacobi"); ax.semilogy(eg, label="Gauss-Seidel")
    ax.set(title="Task 8: Iterative Convergence", xlabel="Iteration", ylabel="Maximum change"); ax.grid(True); ax.legend(); save(fig, "task_08_iterative_convergence.png")
    return {"jacobi": x, "gauss_seidel": xg, "jacobi_iterations": len(ej), "gauss_seidel_iterations": len(eg)}


# ================================ TASK 09 ================================
# Eigenvalues, eigenvectors, and network-node importance.
def task_09_eigenvalues() -> dict:
    A = np.array([[0., 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]])
    vals, vecs = np.linalg.eig(A); i = np.argmax(vals.real); lam = vals[i].real
    scores = abs(vecs[:, i].real); scores /= scores.sum()
    fig, ax = plt.subplots(figsize=(6, 4)); ax.bar(list("ABCD"), scores); ax.set(title="Task 9: Eigenvector Centrality", ylabel="Normalized score"); ax.grid(axis="y"); save(fig, "task_09_eigen_scores.png")
    return {"dominant_eigenvalue": lam, "scores": scores, "verification_error": np.linalg.norm(A @ vecs[:, i] - lam * vecs[:, i])}


# ================================ TASK 10 ================================
# Bisection and fixed-point iteration for nonlinear equilibrium.
def task_10_bisection_fixed_point() -> dict:
    amp = 10.
    f = lambda T: T - 25 - amp * np.exp(-T / 20)
    g = lambda T: 25 + amp * np.exp(-T / 20)
    bis = root_scalar(f, bracket=[20, 40], method="bisect", xtol=1e-10).root
    T = 30.; errors = []
    for k in range(100):
        nxt = g(T); errors.append(abs(nxt - T)); T = nxt
        if errors[-1] < 1e-10: break
    grid = np.linspace(20, 40, 300); fig, ax = plt.subplots(figsize=(8, 4.5)); ax.plot(grid, [f(v) for v in grid], label="f(T)"); ax.axhline(0, color="black", lw=.8); ax.axvline(bis, ls="--", label=f"Root={bis:.3f}°C"); ax.set(title="Task 10: Thermal Equilibrium", xlabel="Temperature (°C)", ylabel="f(T)"); ax.grid(True); ax.legend(); save(fig, "task_10_bisection_root.png")
    return {"bisection_root": bis, "fixed_point_root": T, "fixed_point_iterations": len(errors)}


# ================================ TASK 11 ================================
# Newton–Raphson and secant methods for investment IRR.
def task_11_newton_secant() -> dict:
    cf = np.array([-10000., 3000., 3500., 4000., 2500.])
    npv = lambda r: sum(c / (1 + r) ** t for t, c in enumerate(cf))
    dnpv = lambda r: sum(-t * c / (1 + r) ** (t + 1) for t, c in enumerate(cf) if t)
    newton = root_scalar(npv, fprime=dnpv, x0=.1, method="newton", xtol=1e-12).root
    secant = root_scalar(npv, x0=.05, x1=.2, method="secant", xtol=1e-12).root
    grid = np.linspace(0, .5, 300); fig, ax = plt.subplots(figsize=(8, 4.5)); ax.plot(grid, [npv(v) for v in grid]); ax.axhline(0, color="black", lw=.8); ax.axvline(newton, ls="--", label=f"IRR={newton:.2%}"); ax.set(title="Task 11: NPV and IRR", xlabel="Discount rate", ylabel="NPV ($)"); ax.grid(True); ax.legend(); save(fig, "task_11_irr_npv.png")
    return {"newton_irr": newton, "secant_irr": secant, "npv_at_root": npv(newton)}


# ================================ TASK 12 ================================
# Polynomial/nonlinear system: circle–parabola intersections.
def task_12_nonlinear_system() -> dict:
    def equations(z):
        x, y = z; return [x*x + y*y - 4, y - (x*x - 1)]
    results = [root(equations, guess) for guess in ([1., 1.], [-1., 1.])]
    pts = np.array([r.x for r in results]); grid = np.linspace(-2, 2, 400)
    fig, ax = plt.subplots(figsize=(6, 5)); ax.plot(grid, np.sqrt(4-grid**2), label="Circle"); ax.plot(grid, grid**2 - 1, label="Parabola"); ax.scatter(pts[:,0], pts[:,1], marker="x", s=80, label="Intersections"); ax.set(title="Task 12: Circle–Parabola Intersections", xlabel="x", ylabel="y"); ax.set_ylim(-1.2, 2.1); ax.grid(True); ax.legend(); save(fig, "task_12_nonlinear_system.png")
    return {"intersections": pts, "residual_norms": [np.linalg.norm(equations(r.x)) for r in results]}


# ================================ TASK 13 ================================
# Linear and cubic-spline interpolation.
def task_13_interpolation() -> dict:
    x = np.arange(8, 15, dtype=float); y = np.array([18, 20, 22.5, 24, 25, 25.5, 25.5], float); linear = interp1d(x, y); cubic = CubicSpline(x, y); target = 10.5
    xp = np.linspace(8, 14, 300); fig, ax = plt.subplots(figsize=(8, 4.5)); ax.scatter(x, y, label="Readings"); ax.plot(xp, linear(xp), "--", label="Linear"); ax.plot(xp, cubic(xp), label="Cubic spline"); ax.scatter([target], [linear(target)], marker="x", s=70); ax.set(title="Task 13: Temperature Interpolation", xlabel="Hour", ylabel="Temperature (°C)"); ax.grid(True); ax.legend(); save(fig, "task_13_interpolation.png")
    return {"linear_1030": float(linear(target)), "cubic_1030": float(cubic(target)), "linear_1015": float(linear(10.25)), "cubic_1015": float(cubic(10.25))}


# ================================ TASK 14 ================================
# Numerical differentiation: GPS position to speed.
def task_14_numerical_differentiation() -> dict:
    t = np.arange(7., dtype=float); pos = np.array([0, 4.8, 10.2, 16.1, 22.7, 30, 38.], float); speed = np.gradient(pos, t)
    changed = pos.copy(); changed[3] = 17.1; changed_speed = np.gradient(changed, t)
    fig, ax = plt.subplots(figsize=(8, 4.5)); ax.plot(t, speed, "o-", label="Original speed"); ax.plot(t, changed_speed, "s--", label="Changed data"); ax.set(title="Task 14: Numerical Differentiation", xlabel="Time (s)", ylabel="Speed (m/s)"); ax.grid(True); ax.legend(); save(fig, "task_14_differentiation.png")
    return {"speed": speed, "changed_speed": changed_speed}


# ================================ TASK 15 ================================
# Numerical integration: power to energy.
def task_15_numerical_integration() -> dict:
    t = np.arange(0, 13, 2, dtype=float); p = np.array([.8, 1, 1.4, 1.8, 1.6, 1.2, .9]); changed = p.copy(); changed[3] = 2.2
    trap = np.trapezoid(p, t) if hasattr(np, "trapezoid") else np.trapz(p, t); simp = simpson(p, x=t)
    trap2 = np.trapezoid(changed, t) if hasattr(np, "trapezoid") else np.trapz(changed, t); simp2 = simpson(changed, x=t)
    fig, ax = plt.subplots(figsize=(8, 4.5)); ax.plot(t, p, "o-", label="Original power"); ax.fill_between(t, p, alpha=.2); ax.plot(t, changed, "s--", label="Changed power"); ax.set(title="Task 15: Energy Integration", xlabel="Time (h)", ylabel="Power (kW)"); ax.grid(True); ax.legend(); save(fig, "task_15_integration.png")
    return {"trapezoidal_kwh": trap, "simpson_kwh": simp, "changed_trapezoidal_kwh": trap2, "changed_simpson_kwh": simp2}


# ================================ TASK 16 ================================
# Euler's method for Newton's law of cooling.
def task_16_euler_cooling() -> dict:
    T0, env, k, total = 90., 20., .05, 100.
    fig, ax = plt.subplots(figsize=(8, 4.5)); tt = np.linspace(0, total, 500); ax.plot(tt, env + (T0-env)*np.exp(-k*tt), "k-", label="Exact")
    for dt in [10., 2., .5]:
        n = int(total/dt)+1; t = np.linspace(0, total, n); T = np.zeros(n); T[0] = T0
        for i in range(n-1): T[i+1] = T[i] - dt*k*(T[i]-env)
        ax.plot(t, T, "o--", label=f"Euler dt={dt:g}s")
    ax.set(title="Task 16: Euler Method for Newton Cooling", xlabel="Time (s)", ylabel="Temperature (°C)"); ax.grid(True); ax.legend(); save(fig, "task_16_euler_cooling.png")
    return {"exact_final_temperature": env + (T0-env)*np.exp(-k*total)}


# ================================ TASK 17 ================================
# The report's Task 17 is the Euler method implemented immediately above.
def task_17_ode_transition() -> dict:
    return {"status": "Euler method implemented in Task 16 section above."}


# ================================ TASK 18 ================================
# SciPy solve_ivp for RC-circuit capacitor dynamics.
def task_18_scipy_ode() -> dict:
    R, Vin = 1000., 5.; Cs = [1e-6, 2.2e-6, 4.7e-6]; t_eval = np.linspace(0, .02, 1000)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    for C in Cs:
        sol = solve_ivp(lambda t, v: [(Vin-v[0])/(R*C)], (0, .02), [0.], t_eval=t_eval)
        ax.plot(sol.t*1000, sol.y[0], label=f"C={C*1e6:.1f} µF")
    ax.set(title="Task 17: RC Circuit Charging", xlabel="Time (ms)", ylabel="Capacitor voltage (V)"); ax.grid(True); ax.legend(); save(fig, "task_17_scipy_rc.png")
    return {"final_voltages": {C: float(solve_ivp(lambda t, v: [(Vin-v[0])/(R*C)], (0, .02), [0.], t_eval=[.02]).y[0,-1]) for C in Cs}}


# ================================ TASK 19 ================================
# Logistics fleet allocation using SLSQP and integer search.
def task_19_optimization() -> dict:
    cost = lambda z: 150*z[0] + 250*z[1]
    constraint = {"type": "ineq", "fun": lambda z: 200*z[0] + 400*z[1] - 1500}
    sol = minimize(cost, [5, 5], method="SLSQP", bounds=[(0, None), (0, None)], constraints=constraint)
    feasible = [(150*a+250*b, a, b, 200*a+400*b) for a in range(15) for b in range(15) if 200*a+400*b >= 1500]
    best = min(feasible)
    fig, ax = plt.subplots(figsize=(6, 4)); ax.bar(["Continuous", "Integer"], [sol.fun, best[0]], color=["#7570b3", "#e7298a"]); ax.set(title="Task 18: Fleet Allocation Cost", ylabel="Cost ($)"); ax.grid(axis="y"); save(fig, "task_18_optimization.png")
    return {"continuous": sol.x, "continuous_cost": sol.fun, "best_integer": best}


# ================================ TASK 20 ================================
# Monte Carlo simulation of construction-project budget-overrun risk.
def task_20_monte_carlo() -> dict:
    rng = np.random.default_rng(42); N = 100_000; budget = 180_000.
    total = rng.normal(50000, 5000, N) + rng.normal(80000, 10000, N) + rng.normal(40000, 8000, N)
    over = total > budget; probability = float(over.mean()); running = np.cumsum(over) / np.arange(1, N+1)
    idx = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1
    fig, ax = plt.subplots(figsize=(8, 4.5)); ax.semilogx(idx+1, running[idx], color="tab:red"); ax.axhline(probability, ls="--", color="gray", label=f"Converged={probability:.2%}"); ax.set(title="Task 19: Monte Carlo Budget Overrun Risk", xlabel="Simulations", ylabel="Estimated probability"); ax.grid(True); ax.legend(); save(fig, "task_19_monte_carlo.png")
    return {"probability": probability, "overrun_cases": int(over.sum()), "N": N}


def main() -> None:
    functions = [task_01_numpy_temperature, task_02_vectorization, task_03_floating_point,
                 task_04_matrix_transform, task_05_curve_fit, task_06_linear_system,
                 task_07_lu_decomposition, task_08_iterative_methods, task_09_eigenvalues,
                 task_10_bisection_fixed_point, task_11_newton_secant, task_12_nonlinear_system,
                 task_13_interpolation, task_14_numerical_differentiation, task_15_numerical_integration,
                 task_16_euler_cooling, task_17_ode_transition, task_18_scipy_ode,
                 task_19_optimization, task_20_monte_carlo]
    for number, fn in enumerate(functions, start=1):
        result = fn()
        print(f"Task {number:02d}: {fn.__name__}")
        for key, value in result.items():
            if isinstance(value, np.ndarray) and value.size > 12: value = f"array(shape={value.shape})"
            print(f"  {key}: {value}")
    print(f"\nGraphs written to: {GRAPH_DIR}")


if __name__ == "__main__":
    main()
