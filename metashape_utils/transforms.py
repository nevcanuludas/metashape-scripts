import Metashape

def reset_transform(chunk: Metashape.Chunk):
  """
  Reset the transform matrix of the model to identity.

  Parameters:
    chunk (Metashape.Chunk): The chunk whose transform matrix will be reset.

  Returns:
    None
  """
  chunk.transform.matrix = Metashape.Matrix().diag([1, 1, 1, 1])
  print("Transform matrix has been reset to identity.")
