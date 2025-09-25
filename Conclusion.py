from manim import *
import numpy as np


class ManImExplanation(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Community and conclusion
        community_title = Text(
            "Open Source Community", font_size=32, color="#58C4DD", weight=BOLD
        )
        community_title.to_edge(UP, buff=0.8)

        self.play(Write(community_title), run_time=0.8)

        # Show community features
        features = VGroup(
            Text("📈 Graphs & Charts", font_size=20, color="#FF6B6B"),
            Text("🔢 Math Symbols", font_size=20, color="#4ECDC4"),
            Text("🧮 Specialized Tools", font_size=20, color="#FECA57"),
            Text("🔧 Extensions & Add-ons", font_size=20, color="#FF9FF3"),
        ).arrange(DOWN, buff=0.5)

        self.play(*[Write(feature) for feature in features], run_time=2.0)

        # Final message
        final_message = Text(
            "Animation Built for Coders", font_size=36, color="#FFD700", weight=BOLD
        )
        final_message.move_to(DOWN * 2.5)

        self.play(Write(final_message), run_time=1.5)

        # Create final sparkle effect
        sparkles = VGroup()
        for _ in range(20):
            sparkle = Star(
                n=5,
                outer_radius=0.1,
                fill_color=random_bright_color(),
                fill_opacity=0.8,
            )
            sparkle.move_to([np.random.uniform(-6, 6), np.random.uniform(-3, 3), 0])
            sparkles.add(sparkle)

        self.play(*[DrawBorderThenFill(sparkle) for sparkle in sparkles], run_time=1.0)
        self.play(
            *[sparkle.animate.scale(3).fade(1) for sparkle in sparkles], run_time=2.0
        )

        self.wait(2.0)

        # Final fade
        self.play(
            FadeOut(VGroup(community_title, features, final_message)), run_time=1.5
        )

    # Helper function for random colors
    def random_bright_color():
        colors = [
            "#FF6B6B",
            "#4ECDC4",
            "#45B7D1",
            "#96CEB4",
            "#FECA57",
            "#FF9FF3",
            "#54A0FF",
        ]
        return np.random.choice(colors)
