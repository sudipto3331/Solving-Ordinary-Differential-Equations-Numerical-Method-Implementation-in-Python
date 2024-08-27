# Solving Ordinary Differential Equations Numerical Method Implementation in Python

This repository contains a Python implementation for solving ordinary differential equations (ODEs) using various numerical methods, including the Euler method, Heun's method, the Midpoint method, and the Fourth Order Runge-Kutta (RK4) method. The code also provides a graphical representation of the solution.

### Table of Contents
- [Numerical Methods for ODEs Theory](#numerical-methods-for-odes-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

### Numerical Methods for ODEs Theory
The numerical methods implemented in this code include:

1. **Euler Method**: The simplest numerical method for solving ODEs, which uses the derivative to project forward.
   \[
   y_{n+1} = y_n + h \cdot f(x_n, y_n)
   \]

2. **Heun's Method** (Improved Euler Method): A two-step method that averages slopes at the beginning and end of the interval.
   \[
   k1 = f(x_n, y_n) \\
   k2 = f(x_n + h, y_n + h \cdot k1) \\
   y_{n+1} = y_n + \frac{h}{2} (k1 + k2)
   \]

3. **Midpoint Method**: A second-order method that makes a prediction at the midpoint of the interval and then corrects it.
   \[
   k1 = f(x_n, y_n) \\
   k2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot k1\right) \\
   y_{n+1} = y_n + h \cdot k2
   \]

4. **Fourth Order Runge-Kutta Method (RK4)**: A more accurate method that evaluates the slope at multiple points within the interval.
   \[
   k1 = f(x_n, y_n) \\
   k2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot k1\right) \\
   k3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot k2\right) \\
   k4 = f(x_n + h, y_n + h \cdot k3) \\
   y_{n+1} = y_n + \frac{h}{6} (k1 + 2k2 + 2k3 + k4)
   \]

### Dependencies
This implementation requires the following libraries:
- `matplotlib`: For plotting the results.
- `numpy`: For numerical computations.

### Installation
To install the required libraries, you can use `pip`:
```sh
pip install matplotlib numpy
```

### Usage
1. Clone the repository.
2. Run the script using Python:
    ```sh
    python ode_solver.py
    ```
3. Input the required parameters when prompted:
    - Specify `a1` and `a2` based on the method you wish to use.
    - Enter the order of the ODE.
    - Specify the lower and upper limits of `x`.
    - Enter the initial condition for `y`.
    - Specify the step size `h`.

### Code Explanation
The code defines the differential function `f(x, y)` and computes the solution using different methods based on user input. It then plots the results on a graph.

Below is a snippet from the code illustrating the main logic:

```python
def f(x, y):
   fxy = (-4 * (x**3) + 12 * (x**2) - 20 * x + 8.5)
   return fxy

x0 = float(input("Enter the lower range of x: "))
xfinal = float(input("Enter the higher range of x: "))
y0 = float(input("Enter the lower range of y: "))
h = float(input("Enter the step size: "))
n = int(((xfinal - x0) / h) + 1)
x = np.zeros([n + 1])
y = np.zeros([n + 1])

x[0] = x0
y[0] = y0

# Method selection
if all([a1 == 1, a2 == 0, order == 1]):
    print("Euler method :")
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
elif all([a1 == 0.5, a2 == 0.5, order == 2]):
    print("Heuns method :")
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + k1 * h)
        y[i + 1] = y[i] + h / 2 * (k1 + k2)
elif all([a1 == 0, a2 == 1, order == 2]):
    print("Midpoint method :")
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + k1 * h / 2)
        y[i + 1] = y[i] + k2 * h
elif order == 4:
    print("Fourth order RK method :")
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + k1 * h / 2)
        k3 = f(x[i] + h / 2, y[i] + k2 * h / 2)
        k4 = f(x[i] + h, y[i] + k3 * h)
        y[i + 1] = y[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

plt.figure(1)
plt.plot(x, y)
plt.xlabel('Values of X')
plt.ylabel('Values of Y')
plt.title('Curve of the ODE')
plt.legend(['Graphical Curve'], loc='upper right')
plt.show()
```

### Example
Below is an example of how to use the script:

1. **Run the script**:
    ```sh
    python ode_solver.py
    ```

2. **Enter the input values**:
    ```
    Enter the value of a2 FOR USING, euler a2=0, for heuns a2=0.5, for midpoint a2=1: 0.5
    Enter the value of a1 FOR USING, euler a1=1, for heuns a1=0.5, for midpoint a1=0: 1
    Enter the value of order: 2
    Enter the lower range of x: 0
    Enter the higher range of x: 2
    Enter the lower range of y: 1
    Enter the step size: 0.1
    ```

3. **Output**:
    - The script will compute the numerical solution using the selected method and plot the results:
    ```
    Heuns method :
    [array of y values]
    ```

### Files in the Repository
- `ode_solver.py`: The main script for solving ordinary differential equations using the specified numerical methods.

### Input Parameters
The script prompts for the following input values:
- `a1` and `a2`: Values defining the method to be used.
- Order of the ODE (`order`).
- Lower range of `x` (`x0`).
- Higher range of `x` (`xfinal`).
- Initial condition for `y` (`y0`).
- Step size (`h`).

### Troubleshooting
1. **Method Selection**: Ensure the parameters are correctly set for the desired method to avoid errors.
2. **Function Definition**: The function `f(x, y)` is currently hardcoded. You may modify it to solve different ODEs as needed.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by sudipto3331.

---

This documentation should guide you through understanding, installing, and using the ODE solving script. For further issues or feature requests, please open an issue in the repository. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
