import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

SAVE_FILE = "werte.json"

class MainLayout(BoxLayout):
    def save_values(self):
        data = {
            "Bankdrücken": self.ids.bank_input.text,
            "Schulterdrücken": self.ids.shoulder_input.text,
            "Incline Brust": self.ids.incline_input.text,
            "Seitheben": self.ids.side_input.text,
            "Klimmzüge": self.ids.klimm_input.text,
            "Muscle Ups": self.ids.muscle_input.text,
            "Breites Rudern": self.ids.rudern_input.text,
            "Überzüge": self.ids.ueberzuege_input.text,
            "Reverse Flies": self.ids.revflies_input.text,
            "Bizeps Kurzhantel": self.ids.bizeps_input.text,
            "Trizepsdrücken": self.ids.trizeps_input.text,
            "Hammercurls": self.ids.hammer_input.text,
            "Trizeps überkopf": self.ids.trizepsueber_input.text,
            "Beinpresse": self.ids.beinpresse_input.text,
            "Beinbeuger": self.ids.beinbeuger_input.text,
            "Beinstrecker": self.ids.beinstrecker_input.text,
            "Waden": self.ids.waden_input.text
        }

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

        self.update_output(data)

    def update_output(self, data):
        summary = "\n".join([f"{k}: {v} kg" for k, v in data.items()])
        self.ids.output_label.text = summary

    def on_kv_post(self, base_widget):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                self.ids.bank_input.text = data.get("Bankdrücken", "")
                self.ids.shoulder_input.text = data.get("Schulterdrücken", "")
                self.ids.incline_input.text = data.get("Incline Brust", "")
                self.ids.side_input.text = data.get("Seitheben", "")
                self.ids.klimm_input.text = data.get("Klimmzüge", "")
                self.ids.muscle_input.text = data.get("Muscle Ups", "")
                self.ids.rudern_input.text = data.get("Breites Rudern", "")
                self.ids.ueberzuege_input.text = data.get("Überzüge", "")
                self.ids.revflies_input.text = data.get("Reverse Flies", "")
                self.ids.bizeps_input.text = data.get("Bizeps Kurzhantel", "")
                self.ids.trizeps_input.text = data.get("Trizepsdrücken", "")
                self.ids.hammer_input.text = data.get("Hammercurls", "")
                self.ids.trizepsueber_input.text = data.get("Trizeps überkopf", "")
                self.ids.beinpresse_input.text = data.get("Beinpresse", "")
                self.ids.beinbeuger_input.text = data.get("Beinbeuger", "")
                self.ids.beinstrecker_input.text = data.get("Beinstrecker", "")
                self.ids.waden_input.text = data.get("Waden", "")
                self.update_output(data)

class GymTracker(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    GymTracker().run()