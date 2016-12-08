from common.testcases import *


def suite():
    suite = unittest.TestSuite()

    current_folder = os.getcwd()
    cases_folder = current_folder + "/cases"
    cases_files = os.listdir(cases_folder)
    for case_file in cases_files:
        if case_file.endswith('.py') and case_file.endswith('__.py') is False:
            case_info = case_file.split('.')
            case_name = case_info[0]
            if len(case_name) < 1:
                continue
            case_formal_name = case_name[0].upper() + case_name[1:] + "TestCases"
            import_cases = "from cases.{0:s} import {1:s}".format(case_name, case_formal_name)
            exec(import_cases)
            methods_command ="{0:s}.__dict__".format(case_formal_name)
            results = eval(methods_command)
            for method_name in results:
                if method_name.startswith("test"):
                    suite_command = "suite.addTest({0:s}('{1:s}'))".format(case_formal_name, method_name)
                    exec(suite_command)
    return suite

if __name__ == "__main__":
    print("begin")
    unittest.main(defaultTest="suite")
