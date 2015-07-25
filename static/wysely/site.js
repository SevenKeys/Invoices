wysely = {};
wysely.components = {
    // components add themselves to this dictionary and get initialized on page load
};

wysely.site = {
    // common js things should go here
};

/// common use - add wysely.yourcomponent dictionary, initialize will get called ondocumentload

function executeFunctionByName(functionName, context /*, args */) {
    var args = [].slice.call(arguments).splice(2);
    var namespaces = functionName.split(".");
    var func = namespaces.pop();
    for(var i = 0; i < namespaces.length; i++) {
        context = context[namespaces[i]];
    }

    try {
        context[func].apply(this, args);
    }
    catch(err) {
        /// todo: proper handling is to check if the function exists... maybe later

    }
}

function initPackage(package_name) {
    var namespaces = package_name.split(".");
    context = window;
    for(var i = 0; i < namespaces.length; i++) {
        context = context[namespaces[i]];
    }
    for (var child in context) {
        initPackage(package_name + '.' + child);
    }

    executeFunctionByName(package_name + '.init', window);
}

$(document).ready(function() {
    initPackage('wysely');
});

