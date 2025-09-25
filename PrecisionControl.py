from manim import *
import numpy as np


class PrecisionControl(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Show precision and control capabilities
        precision_title = Text(
            "Precision & Control", font_size=36, color="#58C4DD", weight=BOLD
        )
        precision_title.to_edge(UP, buff=0.8)

        self.play(Write(precision_title), run_time=0.8)

        # Sine wave animation
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": "#888888"},
        )

        sine_function = axes.plot(
            lambda x: np.sin(2 * x), color="#FF6B6B", stroke_width=4
        )

        # Dot tracing the curve
        dot = Dot(color="#FFD700", radius=0.1)
        dot.move_to(axes.coords_to_point(-4, np.sin(-8)))

        # Code snippet showing how it's done
        code_bg = Rectangle(
            width=6,
            height=2,
            fill_color="#1E1E1E",
            fill_opacity=0.9,
            stroke_color="#58C4DD",
        )
        code_bg.to_edge(RIGHT, buff=0.5).shift(DOWN * 2.3)

        code_text = Text(
            "axes.plot(lambda x: sin(2*x))\ndot.move_along_path(sine_curve)",
            font_size=16,
            color="#FFD43B",
            font="Consolas",
        )
        code_text.move_to(code_bg.get_center())

        self.play(Create(axes), run_time=1.0)
        self.play(Create(sine_function), run_time=2.0)
        self.play(FadeIn(VGroup(code_bg, code_text)), run_time=0.8)

        # Animate dot tracing
        self.play(MoveAlongPath(dot, sine_function), run_time=3.0, rate_func=linear)

        self.wait(1.0)
        self.play(
            FadeOut(
                VGroup(precision_title, axes, sine_function, dot, code_bg, code_text)
            ),
            run_time=0.8,
        )
