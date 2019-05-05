# coding=utf-8
from __future__ import absolute_import
from octoprint.server import user_permission

import octoprint.plugin
from flask import make_response

class PlaygroundPlugin(octoprint.plugin.SettingsPlugin,
                   octoprint.plugin.AssetPlugin,
                   octoprint.plugin.TemplatePlugin,
                   octoprint.plugin.SimpleApiPlugin):

    # var
    PlaygroundEnabled = False

    def on_gcode_queuing(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if self.PlaygroundEnabled == True:
            # needed to handle non utf-8 characters
            command_string = cmd.encode('ascii', 'ignore')

        # Send the original unaltered command
        return None

    ## Web-UI - Stuff
    # list all called commands/parameter that are valid to send from the web-ui
    def get_api_commands(self):
        # command with parameters
        return dict(checkboxState=["checkboxValue"],
                    disable=[],
                    abort=[])

    def on_api_command(self, command, data):
        if not user_permission.can():
            return make_response("Insufficient rights", 403)
        if command == "checkboxState":
            self.PlaygroundEnabled = bool(data["checkboxValue"])

    ##~~ AssetPlugin mixin
    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        return dict(
            js=["js/Playground.js"],
            css=["css/Playground.css"],
            less=["less/Playground.less"]
        )

    ##~~ Softwareupdate hook
    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            Playground=dict(
                displayName="Playground Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="OllisGit",
                repo="OctoPrint-CICD_Playground",
                current=self._plugin_version,

                # update method: pip
                #pip="https://github.com/OllisGit/OctoPrint-CICD_Playground/archive/{target_version}.zip"
                pip="https://github.com/OllisGit/OctoPrint-CICD_Playground/archive/{target_version}.zipp"
            )
        )

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Playground Plugin"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = PlaygroundPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.queuing": (__plugin_implementation__.on_gcode_queuing, -1),
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
