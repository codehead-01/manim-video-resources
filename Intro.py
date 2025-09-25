from manim import *


class Intro(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Manim logo-style animation
        manim_logo = SVGMobject("./logos/manim_logo.svg")
        manim_logo.scale(2)
        subtitle = Text("Mathematical Animation Engine", font_size=32, color="#FFFFFF")
        python_badge = Text(
            "Python Library", font_size=20, color="#FFD43B", weight=BOLD
        )

        # Create animated introduction
        self.play(DrawBorderThenFill(manim_logo), run_time=1.5)
        self.play(FadeIn(subtitle.next_to(manim_logo, DOWN, buff=0.5)), run_time=1.0)
        self.play(FadeIn(python_badge.next_to(subtitle, DOWN, buff=0.3)), run_time=0.8)

        self.play(
            FadeOut(VGroup(manim_logo, subtitle, python_badge)),
            run_time=0.8,
        )
