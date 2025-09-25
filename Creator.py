from manim import *


class Creator(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Load logo
        creator_logo = SVGMobject("./logos/3B1B_Logo.svg").scale(2)
        creator_name = Text("3Blue1Brown", font_size=48, color="#3B82F6", weight=BOLD)

        # Position text to the right of the logo
        creator_name.next_to(creator_logo, RIGHT, buff=0.5)

        # Group logo and text together
        logo_group = VGroup(creator_logo, creator_name)

        # Center the whole group (instead of just the logo)
        logo_group.move_to(ORIGIN).shift(LEFT * 1.5)

        # Animate logo + text appearing together
        self.play(DrawBorderThenFill(logo_group), run_time=1.5)

        self.wait(1.0)
