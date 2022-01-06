/*
 * View model for DryRun
 *
 * Author: OllisGit
 * License: AGPLv3
 */
$(function() {
    function PlaygroundViewModel(parameters) {

        var PLUGIN_ID = "Playground";

        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        self.settingsViewModel = parameters[0];

        self.pluginSettings = null;

        ///////////////////////////////////////////////////// START: OctoPrint Hooks

        self.onBeforeBinding = function() {
            // assign current pluginSettings
            self.pluginSettings = self.settingsViewModel.settings.plugins[PLUGIN_ID];
        }

        ///////////////////////////////////////////////////// END: OctoPrint Hooks

    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: PlaygroundViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "settingsViewModel"],
        // Elements to bind to, e.g. #settings_plugin_DryRun, #tab_plugin_DryRun, ...
        elements: [
            "#settings_plugin_Playground",
            document.getElementById("playground_plugin_navbar")
        ]
    });
});
