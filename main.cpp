#include <iostream>

int main() {
    int a, b;
    if (!(std::cin >> a >> b) || b == 0) {
        std::cerr << "Expected two integers and a nonzero divisor\n";
        return 1;
    }
    // Widen before arithmetic to accommodate the full range of int inputs.
    const long long x = a, y = b;
    std::cout << x + y << '\n' << x - y << '\n'
              << x * y << '\n' << x / y << '\n';
}
