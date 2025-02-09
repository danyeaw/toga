from toga.style.pack import COLUMN, END, ROW, RTL, START, Pack

from ..utils import ExampleNode, ExampleViewport, assert_layout


def test_row_box_child_layout():
    root = ExampleNode(
        "container",
        style=Pack(text_direction=RTL, direction=ROW),
        children=[
            ExampleNode(
                "widget_a",
                style=Pack(width=30, height=100, margin_left=32, margin_right=34),
            ),
            ExampleNode(
                "widget_b",
                style=Pack(width=36, height=100, margin_left=38, margin_right=40),
            ),
        ],
    )

    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (210, 100),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (576, 0), "content": (30, 100)},
                {"origin": (468, 0), "content": (36, 100)},
            ],
        },
    )


def test_column_box_child_layout():
    root = ExampleNode(
        "container",
        style=Pack(text_direction=RTL, direction=COLUMN),
        children=[
            ExampleNode(
                "widget_a",
                style=Pack(width=100, height=30, margin_top=32, margin_bottom=34),
            ),
            ExampleNode(
                "widget_b",
                style=Pack(width=100, height=36, margin_top=38, margin_bottom=40),
            ),
        ],
    )

    # Normal size
    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (100, 210),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (0, 32), "content": (100, 30)},
                {"origin": (0, 134), "content": (100, 36)},
            ],
        },
    )


def test_align_items_top():
    root = ExampleNode(
        "root",
        style=Pack(text_direction=RTL, direction=ROW, align_items=START),
        children=[
            ExampleNode("space_filler", style=Pack(width=30, height=100)),
            ExampleNode("widget", style=Pack(width=30, height=30)),
        ],
    )

    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (60, 100),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (610, 0), "content": (30, 100)},
                {"origin": (580, 0), "content": (30, 30)},
            ],
        },
    )


def test_align_items_bottom():
    root = ExampleNode(
        "root",
        style=Pack(text_direction=RTL, direction=ROW, align_items=END),
        children=[
            ExampleNode("space_filler", style=Pack(width=30, height=100)),
            ExampleNode("widget", style=Pack(width=30, height=30)),
        ],
    )

    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (60, 100),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (610, 380), "content": (30, 100)},
                {"origin": (580, 450), "content": (30, 30)},
            ],
        },
    )


def test_align_items_left():
    root = ExampleNode(
        "root",
        style=Pack(text_direction=RTL, direction=COLUMN, align_items=END),
        children=[
            ExampleNode("space_filler", style=Pack(width=100, height=30)),
            ExampleNode("widget", style=Pack(width=30, height=30)),
        ],
    )

    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (100, 60),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (0, 0), "content": (100, 30)},
                {"origin": (0, 30), "content": (30, 30)},
            ],
        },
    )


def test_align_items_right():
    root = ExampleNode(
        "root",
        style=Pack(text_direction=RTL, direction=COLUMN, align_items=START),
        children=[
            ExampleNode("space_filler", style=Pack(width=100, height=30)),
            ExampleNode("widget", style=Pack(width=30, height=30)),
        ],
    )

    root.style.layout(ExampleViewport(640, 480))
    assert_layout(
        root,
        (100, 60),
        (640, 480),
        {
            "origin": (0, 0),
            "content": (640, 480),
            "children": [
                {"origin": (540, 0), "content": (100, 30)},
                {"origin": (610, 30), "content": (30, 30)},
            ],
        },
    )
