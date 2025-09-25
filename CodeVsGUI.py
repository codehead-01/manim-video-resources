from manim import *
import numpy as np


class CodeVsGUI(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Compare code-driven vs GUI tools
        comparison_title = Text(
            "Code-Driven vs GUI Tools", font_size=32, color="#58C4DD", weight=BOLD
        )
        comparison_title.to_edge(UP, buff=0.8)

        self.play(Write(comparison_title), run_time=0.8)

        # Code side
        code_side = VGroup()
        code_box = Rectangle(
            width=5,
            height=4,
            fill_color="#1E1E1E",
            fill_opacity=0.9,
            stroke_color="#58C4DD",
        )
        code_title = Text("Manim (Code)", font_size=20, color="#58C4DD", weight=BOLD)
        code_title.next_to(code_box, UP, buff=0.2)

        code_benefits = VGroup(
            Text("✓ Precise control", font_size=14, color="#00FF00"),
            Text("✓ Reproducible", font_size=14, color="#00FF00"),
            Text("✓ Flexible", font_size=14, color="#00FF00"),
            Text("✓ Version control", font_size=14, color="#00FF00"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        code_benefits.move_to(code_box.get_center())

        code_side.add(code_box, code_title, code_benefits)
        code_side.move_to(LEFT * 3)

        # GUI side
        gui_side = VGroup()
        gui_box = Rectangle(
            width=5,
            height=4,
            fill_color="#2D2D2D",
            fill_opacity=0.9,
            stroke_color="#FF6B6B",
        )
        gui_title = Text(
            "After Effects (GUI)", font_size=20, color="#FF6B6B", weight=BOLD
        )
        gui_title.next_to(gui_box, UP, buff=0.2)

        gui_features = VGroup(
            Text("• Visual interface", font_size=14, color="#CCCCCC"),
            Text("• Learning curve", font_size=14, color="#CCCCCC"),
            Text("• Limited precision", font_size=14, color="#CCCCCC"),
            Text("• Manual tweaking", font_size=14, color="#CCCCCC"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        gui_features.move_to(gui_box.get_center())

        gui_side.add(gui_box, gui_title, gui_features)
        gui_side.move_to(RIGHT * 3)

        self.play(FadeIn(code_side), run_time=1.0)
        self.play(FadeIn(gui_side), run_time=1.0)

        # Show advantage: 50 shapes rotating in sync
        demo_text = Text(
            "Need 50 shapes rotating perfectly in sync?", font_size=20, color="#FFD700"
        )
        demo_text.move_to(DOWN * 2.5)

        self.play(Write(demo_text), run_time=1.0)

        # Create 50 small shapes
        shapes = VGroup()
        for i in range(50):
            if i % 2 == 0:
                shape = Circle(
                    radius=0.05, color=random_bright_color(), fill_opacity=0.8
                )
            else:
                shape = Square(
                    side_length=0.1, color=random_bright_color(), fill_opacity=0.8
                )

            angle = i * (2 * PI / 50)
            shape.move_to(2 * np.array([np.cos(angle), np.sin(angle), 0]))
            shapes.add(shape)

        self.play(*[DrawBorderThenFill(shape) for shape in shapes], run_time=1.0)
        self.play(Rotate(shapes, angle=2 * PI), run_time=2.0)

        self.wait(1.0)
        self.play(
            FadeOut(VGroup(comparison_title, code_side, gui_side, demo_text, shapes)),
            run_time=0.8,
        )
