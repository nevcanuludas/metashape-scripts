import Metashape
from metashape_utils.transforms import reset_transform

def main():
  ### Load your project file
  # doc = Metashape.Document()
  # doc.open("C:/your/path/to/project.psx")  # Update this path

  ### Use currently open project
  doc = Metashape.app.document
  
  if not doc:
    print("No project is currently open.")
    return

  chunk = doc.chunk

  if not chunk:
    print("No chunk is currently loaded in Metashape.")
    return

  # Apply transform reset
  reset_transform(chunk)

  # Save the project
  doc.save()
  print("Project saved successfully.")

if __name__ == "__main__":
  main()
