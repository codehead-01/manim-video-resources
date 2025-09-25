from manim import *


class ManImExplanation(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Write the theorem
        theorem = Text("a² + b² = c²", font_size=40, color="#FFD700", weight=BOLD)
        theorem.move_to(UP * 3)

        self.play(Write(theorem), run_time=1.5)

        # Create right triangle
        triangle = Polygon(
            [-2, -1, 0],
            [1, -1, 0],
            [-2, 1.5, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_color="#333333",
            fill_opacity=0.3,
        )

        # Add side labels
        a_label = Text("a", font_size=24, color="#FF6B6B", weight=BOLD).move_to(
            [-2.3, 0.2, 0]
        )
        b_label = Text("b", font_size=24, color="#4ECDC4", weight=BOLD).move_to(
            [-0.5, -1.3, 0]
        )
        c_label = Text("c", font_size=24, color="#FECA57", weight=BOLD).move_to(
            [-0.3, 0.5, 0]
        )

        self.play(DrawBorderThenFill(triangle), run_time=1.0)
        self.play(Write(VGroup(a_label, b_label, c_label)), run_time=1.0)

        # Create squares on each side
        square_a = Square(side_length=2.5, fill_color="#FF6B6B", fill_opacity=0.6)
        square_a.next_to(triangle, LEFT, buff=0).align_to(triangle, DOWN)

        square_b = Square(side_length=3, fill_color="#4ECDC4", fill_opacity=0.6)
        square_b.next_to(triangle, DOWN, buff=0).align_to(triangle, LEFT)

        square_c = Square(side_length=3.91, fill_color="#FECA57", fill_opacity=0.6)
        square_c.move_to([0.75, 1.8, 0])
        square_c.rotate(-PI / 4.5)

        # Animate squares forming
        self.play(GrowFromCenter(square_a), run_time=1.0)
        self.play(GrowFromCenter(square_b), run_time=1.0)
        self.play(GrowFromCenter(square_c), run_time=1.0)

        # Add area labels
        area_a = Text("a²", font_size=20, color=WHITE, weight=BOLD).move_to(
            square_a.get_center()
        )
        area_b = Text("b²", font_size=20, color=WHITE, weight=BOLD).move_to(
            square_b.get_center()
        )
        area_c = Text("c²", font_size=20, color=WHITE, weight=BOLD).move_to(
            square_c.get_center()
        )

        self.play(Write(VGroup(area_a, area_b, area_c)), run_time=1.0)

        self.wait(1.5)

        # Clear scene
        all_pyth = VGroup(
            theorem,
            triangle,
            a_label,
            b_label,
            c_label,
            square_a,
            square_b,
            square_c,
            area_a,
            area_b,
            area_c,
        )
        self.play(FadeOut(all_pyth), run_time=1.0)
