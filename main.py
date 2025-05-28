import Metashape
from metashape_utils.transforms import reset_transform

def main():
  # Load your project file
  doc = Metashape.Document()
  doc.open("C:/your/path/to/project.psx")  # Update this path
  chunk = doc.chunk

  # Apply transform reset
  reset_transform(chunk)

  # Save the project
  doc.save()
  print("Project saved successfully.")

if __name__ == "__main__":
  main()
