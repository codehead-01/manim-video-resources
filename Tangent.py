from manim import *


class Tangent(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=10,
            y_length=6,
            axis_config={
                "color": "#888888",
                "stroke_width": 2,
            },
            tips=True,
        )

        # Create parabola function
        def parabola_func(x):
            return x**2

        def derivative_func(x):
            return 2 * x  # derivative of x^2

        # Create the parabola
        parabola = axes.plot(
            parabola_func,
            color="#4ECDC4",
            stroke_width=4,
            x_range=[-2.5, 2.5],
        )

        # Add function label
        func_label = Text("f(x) = x²", font_size=24, color="#4ECDC4", weight=BOLD)
        func_label.move_to(axes.coords_to_point(1, 3.5))

        # Setup scene
        self.play(Create(axes), run_time=1.5)
        self.play(Create(parabola), Write(func_label), run_time=2.0)

        # Create point on parabola that will move
        x_tracker = ValueTracker(-2)

        # Point that moves along the parabola
        moving_point = always_redraw(
            lambda: Dot(
                axes.coords_to_point(
                    x_tracker.get_value(), parabola_func(x_tracker.get_value())
                ),
                color="#FF6B6B",
                radius=0.1,
            )
        )

        # Tangent line that updates based on point position
        tangent_line = always_redraw(
            lambda: self.get_tangent_line(
                axes, x_tracker.get_value(), parabola_func, derivative_func
            )
        )

        # Add slope text that updates
        slope_text = always_redraw(
            lambda: self.get_slope_text(x_tracker.get_value(), derivative_func)
        )

        # Show initial point and tangent line
        self.play(FadeIn(moving_point), run_time=0.8)
        self.play(Create(tangent_line), run_time=1.0)
        self.play(Write(slope_text), run_time=0.8)

        # Animate the point sliding across the parabola
        self.play(x_tracker.animate.set_value(2), run_time=6.0, rate_func=smooth)

        # Pause at the end
        self.wait(1.0)

        # Create multiple tangent lines at different points
        x_values = [-1.5, -0.5, 0.5, 1.5]
        multiple_tangents = VGroup()
        multiple_points = VGroup()

        for x_val in x_values:
            point = Dot(
                axes.coords_to_point(x_val, parabola_func(x_val)),
                color="#FF6B6B",
                radius=0.08,
            )
            tangent = self.get_tangent_line(
                axes, x_val, parabola_func, derivative_func, opacity=0.6
            )
            multiple_tangents.add(tangent)
            multiple_points.add(point)

        self.play(
            *[Create(tangent) for tangent in multiple_tangents],
            *[FadeIn(point) for point in multiple_points],
            run_time=2.0,
        )

        # Final message
        final_message = Text(
            "Each point has its own slope!\nThat's what derivatives measure.",
            font_size=20,
            color="#00FF00",
            weight=BOLD,
        )
        final_message.move_to(DOWN * 2.8)

        self.play(Write(final_message), run_time=1.5)

        # Code snippet showing how easy it is
        code_box = Rectangle(
            width=8,
            height=1.5,
            fill_color="#1E1E1E",
            fill_opacity=0.9,
            stroke_color="#58C4DD",
        )
        code_box.to_edge(DOWN, buff=0.3)

        code_text = Text(
            "# Just a few lines of code!\nparabola = axes.plot(lambda x: x**2)\ntangent_line.animate_sliding(parabola)",
            font_size=14,
            color="#FFD43B",
            font="Consolas",
        )
        code_text.move_to(code_box.get_center())

        self.play(
            FadeIn(VGroup(code_box, code_text)), FadeOut(final_message), run_time=1.5
        )

        self.wait(2.0)

        # Clear everything
        all_objects = VGroup(
            axes,
            parabola,
            func_label,
            moving_point,
            tangent_line,
            slope_text,
            multiple_tangents,
            multiple_points,
            code_box,
            code_text,
        )
        self.play(FadeOut(all_objects), run_time=1.5)

    def get_tangent_line(self, axes, x_val, func, derivative_func, length=2, opacity=1):
        """Create a tangent line at a specific x value"""
        y_val = func(x_val)
        slope = derivative_func(x_val)

        # Calculate line endpoints
        dx = length / 2
        start_x = x_val - dx
        end_x = x_val + dx
        start_y = y_val - slope * dx
        end_y = y_val + slope * dx

        # Create line
        tangent_line = Line(
            axes.coords_to_point(start_x, start_y),
            axes.coords_to_point(end_x, end_y),
            color="#FF6B6B",
            stroke_width=3,
            stroke_opacity=opacity,
        )

        return tangent_line

    def get_slope_text(self, x_val, derivative_func):
        """Create text showing the current slope"""
        slope = derivative_func(x_val)
        slope_text = Text(
            f"Slope = {slope:.1f}", font_size=20, color="#FF6B6B", weight=BOLD
        )
        slope_text.move_to(UP * 2.5 + RIGHT * 6)
        return slope_text


if __name__ == "__main__":
    # To render: manim -pql tangent_line_demo.py TangentLineDemo
    pass
