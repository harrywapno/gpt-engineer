from compiler import Compiler
from gui import GUI
from code_generator import CodeGenerator

def main():
    compiler = Compiler()
    gui = GUI()
    code_generator = CodeGenerator()

    while True:
        user_input = gui.get_user_input()
        if user_input == "compile":
            code = gui.get_code()
            compiled_code = compiler.compile(code)
            gui.display_compiled_code(compiled_code)
        elif user_input == "generate":
            generated_code = code_generator.generate()
            gui.display_generated_code(generated_code)
        elif user_input == "exit":
            break

if __name__ == "__main__":
    main()
