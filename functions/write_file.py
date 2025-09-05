import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Cannot create file "{file_path}." {e}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file_path given content. If the file exists, it will be overwritten, otherwise a new file will be created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to be written",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file",
            )
        },
        required=["file_path", "content"],
    ),
)