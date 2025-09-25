from manim import *
import numpy as np


class Equations(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#0C0C0C"

        self.equation_to_graph_demo()  # New powerful demonstration

    def equation_to_graph_demo(self):
        # Show Manim's power: equation transforming to graph
        power_title = Text(
            "Equations Come Alive", font_size=36, color="#FFD700", weight=BOLD
        )
        power_title.to_edge(UP, buff=0.8)

        self.play(Write(power_title), run_time=1.0)

        # Complex mathematical function
        complex_equation = Text(
            "f(x) = sin(2x) × cos(x) + 0.5×sin(5x)",
            font_size=32,
            color="#58C4DD",
            weight=BOLD,
        )
        complex_equation.move_to(ORIGIN)

        # Write the equation with dramatic effect
        self.play(Write(complex_equation), run_time=2.5)
        self.wait(0.8)

        # Show transformation message
        transform_text = Text("Watch it transform...", font_size=24, color="#FFD700")
        transform_text.move_to(DOWN * 1.5)

        self.play(FadeIn(transform_text), run_time=1.0)
        self.wait(0.5)

        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
            axis_config={
                "color": "#888888",
                "stroke_width": 2,
            },
            tips=False,
        )

        # Define the complex function
        def complex_func(x):
            return np.sin(2 * x) * np.cos(x) + 0.5 * np.sin(5 * x)

        # Create the graph
        function_graph = axes.plot(
            complex_func,
            color="#FF6B6B",
            stroke_width=4,
            x_range=[-4, 4],
        )

        # Animate transformation: equation shrinks and moves up
        self.play(
            complex_equation.animate.scale(0.6).move_to(UP * 2.8),
            FadeOut(transform_text),
            run_time=1.5,
        )

        # Axes appear
        self.play(Create(axes), run_time=1.5)

        # Graph draws itself smoothly
        self.play(Create(function_graph), run_time=3.0)

        # Add axis labels
        x_label = Text("x", font_size=20, color="#CCCCCC").next_to(
            axes.x_axis.get_end(), RIGHT
        )
        y_label = Text("f(x)", font_size=20, color="#CCCCCC").next_to(
            axes.y_axis.get_end(), UP
        )

        self.play(Write(x_label), Write(y_label), run_time=0.8)

        # Add animated dot tracing the function
        dot = Dot(color="#FFD700", radius=0.08)
        dot.move_to(axes.coords_to_point(-4, complex_func(-4)))

        # Trace along the curve
        self.play(FadeIn(dot), run_time=0.3)
        self.play(MoveAlongPath(dot, function_graph), run_time=4.0, rate_func=linear)

        # Add dramatic conclusion
        conclusion_text = Text(
            "From Abstract to Visual!", font_size=28, color="#00FF00", weight=BOLD
        )
        conclusion_text.move_to(DOWN * 2.8)

        self.play(Write(conclusion_text), run_time=1.2)

        # Create sparkle effect around the graph
        sparkles = VGroup()
        for _ in range(15):
            sparkle = Star(
                n=5, outer_radius=0.1, fill_color="#FFD700", fill_opacity=0.8
            )
            # Position sparkles around the graph
            x_val = np.random.uniform(-4, 4)
            y_val = complex_func(x_val) + np.random.uniform(-0.5, 0.5)
            sparkle.move_to(axes.coords_to_point(x_val, y_val))
            sparkles.add(sparkle)

        self.play(*[DrawBorderThenFill(sparkle) for sparkle in sparkles], run_time=0.8)
        self.play(
            *[sparkle.animate.scale(2).fade(1) for sparkle in sparkles], run_time=1.2
        )

        self.wait(1.0)

        # Clear everything for next scene
        all_elements = VGroup(
            power_title,
            complex_equation,
            axes,
            function_graph,
            x_label,
            y_label,
            dot,
            conclusion_text,
        )
        self.play(FadeOut(all_elements), run_time=1.2)


if __name__ == "__main__":
    # To render this animation, save as manim_explanation.py and run:
    # manim -pql manim_explanation.py ManImExplanation
    pass
