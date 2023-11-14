from flask import Flask, render_template
import random

app = Flask(__name__)


def monte_carlo_simulation(num_simulations):
    inside_circle = 0
    total_points = num_simulations

    for _ in range(num_simulations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x ** 2 + y ** 2

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / total_points) * 4
    return pi_estimate, total_points


@app.route('/monte_carlo/<int:num_simulations>', methods=['GET'])
def run_monte_carlo_simulation(num_simulations):
    pi_estimate, total_points = monte_carlo_simulation(num_simulations)
    return render_template('result.html', pi_estimate=pi_estimate, total_points=total_points)


if __name__ == '__main__':
    app.run(debug=True)
