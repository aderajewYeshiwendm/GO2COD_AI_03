from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize game state
game_state = {
    "low": 1,
    "high": 100,
    "guess": 50,
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reset", methods=["POST"])
def reset_game():
    """Reset the game state."""
    game_state["low"] = 1
    game_state["high"] = 100
    game_state["guess"] = 50
    return jsonify({"message": "Game reset", "guess": game_state["guess"]})

@app.route("/process_hint", methods=["POST"])
def process_hint():
    """Process user hint."""
    data = request.json
    hint = data["hint"]

    if hint == "too low":
        game_state["low"] = game_state["guess"] + 1
    elif hint == "too high":
        game_state["high"] = game_state["guess"] - 1

    # Calculate the next guess
    game_state["guess"] = (game_state["low"] + game_state["high"]) // 2

    return jsonify({"guess": game_state["guess"]})

if __name__ == "__main__":
    app.run(debug=True)
