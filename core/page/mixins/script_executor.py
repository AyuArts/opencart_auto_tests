import allure


class ScriptExecutor:
    @allure.step("Execute JS: {script}")
    def _execute_script(self, script, *args):
        self.log.info(f"Executing JS script: {script}")
        return self._driver.execute_script(script, *args)
