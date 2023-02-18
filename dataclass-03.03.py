from dataclasses import make_dataclass, field

CarData = make_dataclass("CarData",[("model", str),
						            "max_speed",
						            ("price", float, field(default=0))],
						namespace={"get_max_speed": lambda self: self.max_speed})
