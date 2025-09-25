from manim import *
import numpy as np


class StunningAnimation(ThreeDScene):
    def construct(self):
        # Background color
        self.camera.background_color = "#111111"

        # Title text
        title = Text(
            "Math Meets Art", font_size=42, color="#FFD700", weight=BOLD
        ).to_edge(UP)

        self.play(Write(title), run_time=1.5)

        # Create glowing grid
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            axis_config={"color": "#666666"},
        )
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            background_line_style={
                "stroke_color": "#444444",
                "stroke_width": 1,
            },
        ).scale(0.8)

        self.play(Create(grid), run_time=2.0)

        # Camera intro move
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        # Define a parametric surface
        surface = Surface(
            lambda u, v: np.array(
                [np.sin(u) * np.cos(v), np.sin(u) * np.sin(v), np.cos(u)]
            ),
            u_range=[0, PI],
            v_range=[0, 2 * PI],
            resolution=(32, 32),
            fill_opacity=0.8,
            checkerboard_colors=[BLUE_D, PURPLE_D],
        ).scale(2)

        # Transition grid → surface
        self.play(FadeOut(grid), run_time=1.0)
        self.play(Create(surface), run_time=2.5)

        # Rotate surface
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)

        # Outro text
        outro = Text(
            "Beautiful, Precise, Manim.", font_size=36, color="#00FFAA", weight=BOLD
        ).to_edge(DOWN)

        self.play(Write(outro), run_time=1.5)
        self.wait(2)
