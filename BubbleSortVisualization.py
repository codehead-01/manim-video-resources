from manim import *


class BubbleSortVisualization(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Title
        title = Text(
            "Bubble Sort Algorithm", font_size=36, color="#ffffff", weight=BOLD
        )
        title.to_edge(UP, buff=0.8)

        self.play(Write(title), run_time=1.0)

        # Initial array to sort
        array_values = [64, 34, 25, 12, 22, 11, 90]

        # Create bars representing array elements
        bars = self.create_bars(array_values)

        self.play(*[DrawBorderThenFill(bar) for bar in bars], run_time=1.5)

        # Add value labels on bars
        value_labels = self.create_value_labels(array_values, bars)
        self.play(*[Write(label) for label in value_labels], run_time=1.0)

        self.wait(0.5)

        # Start bubble sort animation
        self.bubble_sort_animate(array_values, bars, value_labels)

        self.wait(2.0)

    def create_bars(self, values):
        bars = VGroup()
        max_val = max(values)

        baseline_y = -2  # all bars will sit on this baseline

        for i, val in enumerate(values):
            height = (val / max_val) * 3

            bar = Rectangle(
                width=0.8,
                height=height,
                fill_color="#4ECDC4",
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2,
            )

            # Position bars horizontally and align bottom at baseline
            x_pos = (i - len(values) / 2 + 0.5) * 1.2
            bar.move_to([x_pos, baseline_y + height / 2, 0])

            bars.add(bar)

        return bars

    def create_value_labels(self, values, bars):
        """Create text labels showing values on bars"""
        labels = VGroup()

        for i, (val, bar) in enumerate(zip(values, bars)):
            label = Text(str(val), font_size=16, color=WHITE, weight=BOLD)
            label.move_to(bar.get_center())
            labels.add(label)

        return labels

    def bubble_sort_animate(self, values, bars, labels):
        """Animate the bubble sort algorithm"""
        n = len(values)
        array_copy = values.copy()

        for i in range(n):
            for j in range(0, n - i - 1):
                # Highlight the two bars being compared
                self.play(
                    bars[j].animate.set_fill(color="#FF6B6B", opacity=1),
                    bars[j + 1].animate.set_fill(color="#FF6B6B", opacity=1),
                    run_time=0.3,
                )

                # Check if we need to swap
                if array_copy[j] > array_copy[j + 1]:
                    # Swap in our array copy
                    array_copy[j], array_copy[j + 1] = array_copy[j + 1], array_copy[j]

                    # Animate the swap
                    self.swap_bars(bars[j], bars[j + 1], labels[j], labels[j + 1])

                    # Swap the bars and labels in our groups too
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]

                # Reset colors after comparison
                self.play(
                    bars[j].animate.set_fill(color="#4ECDC4", opacity=0.8),
                    bars[j + 1].animate.set_fill(color="#4ECDC4", opacity=0.8),
                    run_time=0.2,
                )

            # Mark the last element as sorted (green)
            self.play(
                bars[n - 1 - i].animate.set_fill(color="#00FF00", opacity=0.8),
                run_time=0.3,
            )

        # Mark the first element as sorted too
        self.play(bars[0].animate.set_fill(color="#00FF00", opacity=0.8), run_time=0.3)

    def swap_bars(self, bar1, bar2, label1, label2):
        """Animate swapping of two bars and their labels"""
        # Get positions
        pos1 = bar1.get_center()
        pos2 = bar2.get_center()

        # Swap only the x coordinates (keep the same baseline y)
        new_pos1 = [pos2[0], pos1[1], 0]
        new_pos2 = [pos1[0], pos2[1], 0]

        new_label_pos1 = [pos2[0], label1.get_center()[1], 0]
        new_label_pos2 = [pos1[0], label2.get_center()[1], 0]

        # Animate
        self.play(
            bar1.animate.move_to(new_pos1),
            bar2.animate.move_to(new_pos2),
            label1.animate.move_to(new_label_pos1),
            label2.animate.move_to(new_label_pos2),
            run_time=0.6,
        )


if __name__ == "__main__":
    pass
