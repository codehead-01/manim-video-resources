from manim import *
import numpy as np


class MathCS(Scene):
    def construct(self):
        self.camera.background_color = "#111111"

        # Create a coordinate plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            axis_config={"stroke_color": GRAY, "stroke_width": 1},
            background_line_style={"stroke_color": "#222222", "stroke_width": 1},
        )
        self.play(FadeIn(plane), run_time=1)

        # Draw a sine wave
        sine_wave = always_redraw(
            lambda: FunctionGraph(
                lambda x: np.sin(x), x_range=[-6, 6], color=BLUE, stroke_width=3
            )
        )
        self.play(Create(sine_wave), run_time=2)

        # Add some floating binary digits
        # Add some floating binary digits
        digits = VGroup(
            *[
                Text(
                    str(np.random.choice(["0", "1"])), font_size=28, color=GREEN
                ).move_to([np.random.uniform(-5, 5), np.random.uniform(-2, 2), 0])
                for _ in range(12)
            ]
        )

        self.play(
            LaggedStart(*[FadeIn(d) for d in digits], lag_ratio=0.1), run_time=1.5
        )

        # Animate digits slowly drifting downward
        self.play(*[d.animate.shift(DOWN * 0.5) for d in digits], run_time=1.5)

        # Fade everything out smoothly
        self.play(FadeOut(VGroup(plane, sine_wave, digits)), run_time=1.5)
