import glob
import os
import subprocess


def compile_protos(proto_dir, output_dir):
    proto_files = glob.glob(os.path.join(proto_dir, '*.proto'))
    for proto_file in proto_files:
        proto_file = os.path.normpath(proto_file)
        command = [
            f"python -m grpc_tools.protoc -I{proto_dir} --python_out={output_dir} --grpc_python_out={output_dir}",
            proto_file
        ]
        try:
            # subprocess.run("python --version", check=True)
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {proto_file}")
            print(e)
            print(e.output)
            raise
        except Exception as e:
            print(f"Error compiling {proto_file}")
            print(e)
            raise

    # Ensure the output directory is a package
    init_file = os.path.join(output_dir, '__init__.py')
    if not os.path.exists(init_file):
        open(init_file, 'w').close()

    # Fix import paths in generated files
    generated_files = glob.glob(os.path.join(output_dir, '*.py'))
    for generated_file in generated_files:
        with open(generated_file, 'r') as file:
            content = file.read()

        # Replace all absolute imports with relative imports
        updated_content = content
        for proto_file in proto_files:
            proto_name = os.path.splitext(os.path.basename(proto_file))[0]
            original_import = f'import {proto_name}_pb2 as {proto_name}__pb2'
            relative_import = f'from . import {proto_name}_pb2 as {proto_name}__pb2'
            updated_content = updated_content.replace(original_import, relative_import)

        with open(generated_file, 'w') as file:
            file.write(updated_content)


if __name__ == '__main__':
    proto_dir = os.path.normpath('/app/grpc/protos')
    output_dir = os.path.normpath('/app/grpc/generated')
    os.makedirs(output_dir, exist_ok=True)
    compile_protos(proto_dir, output_dir)
