from manim import *


class ScenesMobjects(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#111111"

        # Scene visualization
        scene_frame = Rectangle(
            width=8, height=5, stroke_color="#FFD700", stroke_width=3
        )
        scene_label = Text("Scene (Canvas)", font_size=20, color="#FFD700", weight=BOLD)
        scene_label.next_to(scene_frame, UP, buff=0.2)

        self.play(Create(scene_frame), Write(scene_label), run_time=1.0)

        # Create various mobjects
        mobjects_data = [
            {
                "obj": Circle(radius=0.5, color="#FF6B6B"),
                "label": "Circle",
                "pos": [-2.5, 1, 0],
            },
            {
                "obj": Square(side_length=1, color="#4ECDC4"),
                "label": "Square",
                "pos": [0, 1, 0],
            },
            {
                "obj": Text("Hello!", font_size=24, color="#FECA57"),
                "label": "Text",
                "pos": [2.5, 1, 0],
            },
            {
                "obj": Text(
                    "∑(1/n²) = π²/6", font_size=20, color="#FF9FF3", weight=BOLD
                ),
                "label": "Equation",
                "pos": [0, -1, 0],
            },
        ]

        mobject_groups = VGroup()

        for data in mobjects_data:
            obj = data["obj"]
            label = Text(data["label"], font_size=16, color=WHITE)
            obj.move_to(data["pos"])
            label.next_to(obj, DOWN, buff=0.3)

            group = VGroup(obj, label)
            mobject_groups.add(group)

        # Animate mobjects appearing
        for group in mobject_groups:
            self.play(FadeIn(group), run_time=0.6)

        # Add mobject explanation
        mobject_desc = Text(
            "Mobjects = Mathematical Objects", font_size=18, color="#CCCCCC"
        )
        mobject_desc.move_to(DOWN * 2.8)

        self.play(Write(mobject_desc), run_time=0.8)

        self.wait(3.0)
        self.play(
            FadeOut(
                VGroup(
                    scene_frame,
                    scene_label,
                    mobject_groups,
                    mobject_desc,
                )
            ),
            run_time=0.8,
        )
