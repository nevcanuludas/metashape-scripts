# 📋 Project TODO List: Metashape Automation Scripts

This document tracks the ongoing and planned tasks for improving and extending the Metashape script utilities.

---

## ✅ Completed

- [x] Created project repository
- [x] Built modular project structure (`main.py`, `metashape_utils/`)
- [x] Implemented `reset_transform()` function

---

## 🧩 Utility Functions

- [ ] `rotate_z(chunk, degrees)`  
  Rotate the model around the Z-axis by the given number of degrees.

- [ ] `align_to_top_view(chunk)`  
  Align the model so that it faces upright when viewed from the top.

- [ ] `center_model(chunk)`  
  Move the model to the scene's origin (0,0,0).

- [ ] `scale_model(chunk, scale_factor)`  
  Uniformly scale the model to a specified factor.

---

## ⚙️ CLI Support (via `argparse`)

- [ ] Add command-line interface using `argparse`
- [ ] Add support for flags:
  - `--project`: path to `.psx` file
  - `--reset`: apply transform reset
  - `--rotate_z <degrees>`: rotate model around Z-axis

- [ ] Handle invalid or missing input gracefully
- [ ] Update `README.md` with usage examples

---

## 📚 Documentation

- [ ] Write full English docstrings for each utility function
- [ ] Expand `README.md`:
  - [ ] Project overview
  - [ ] Installation instructions
  - [ ] Usage examples
  - [ ] How to contribute section

---

## 🧪 Testing & Error Handling

- [ ] Build a test `.psx` project for development
- [ ] Add `try/except` blocks for key operations (e.g., missing chunk, invalid transform)
- [ ] Add verbose/debug mode output (optional)

---

## 🔁 Future Improvements

- [ ] Read project settings from config file (`.json`, `.ini`, or `.yaml`)
- [ ] Add optional GUI (Tkinter or PyQt)
- [ ] Setup GitHub Actions for linting/testing
- [ ] Implement basic unit tests (if applicable)

---

## 🗂️ Notes

You can move tasks from this file into GitHub Issues or a Project Board to better track progress as the codebase grows.
