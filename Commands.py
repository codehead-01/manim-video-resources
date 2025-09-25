from manim import *


class Commands(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        commands_title = Text(
            "Animation Commands", font_size=36, color="#58C4DD", weight=BOLD
        )
        commands_title.to_edge(UP, buff=0.8)

        self.play(Write(commands_title), run_time=0.8)

        # Create objects for demonstration
        demo_text = Text("Hello Manim!", font_size=48, color="#FFD700")
        demo_circle = Circle(radius=1.5, color="#FF6B6B", fill_opacity=0.3)
        demo_square = Square(side_length=2, color="#4ECDC4", fill_opacity=0.3)

        # Position objects
        demo_text.move_to(UP * 2)
        demo_circle.move_to(LEFT * 3)
        demo_square.move_to(RIGHT * 3)

        # Show Write command
        write_label = Text("Write(text)", font_size=20, color="#CCCCCC")
        write_label.move_to(UP * 1.2)

        self.play(FadeIn(write_label), run_time=0.5)
        self.play(Write(demo_text), run_time=2.0)

        # Show FadeIn command
        fadein_label = Text("FadeIn(circle)", font_size=20, color="#CCCCCC")
        fadein_label.move_to(LEFT * 3 + DOWN * 2)

        self.play(FadeIn(fadein_label), run_time=0.5)
        self.play(FadeIn(demo_circle), run_time=1.5)

        # Show Transform command
        transform_label = Text(
            "Transform(circle, square)", font_size=20, color="#CCCCCC"
        )
        transform_label.move_to(RIGHT * 3 + DOWN * 2)

        self.play(FadeIn(transform_label), run_time=0.5)
        self.play(Transform(demo_circle, demo_square), run_time=2.0)

        self.wait(1.0)
        self.play(
            FadeOut(
                VGroup(
                    commands_title,
                    demo_text,
                    demo_circle,
                    write_label,
                    fadein_label,
                    transform_label,
                )
            ),
            run_time=0.8,
        )
