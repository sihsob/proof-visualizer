$('.dropdown-menu a').on('click', function(){
    $('.dropdown-toggle').html($(this).html() + '<span class="caret"></span>');
});

$(document).ready(function() {
    var prevReferences = null;
    var logicRule = null;

    // requires some nodes be highlighted
    // already and sets prevReferences
    function onCreateReferences(e) {
        e.preventDefault();
        console.log("onCreateReferences()");
        if (prevReferences !== null)
            return;
        if (logicRule !== null)
            return;

        var inferenceRules = $('#inference-rule').find(":selected").val();
        console.log(" -- got inference rule '" + inferenceRules + "'");

        // TODO: get highlighted nodes,
        // set prevReferences
        // TODO: set logicRule
    }

    // requires prevReferences to have a
    // non-null value, and that a single
    // node be highlighted. Sets go.js pane
    // accordingly
    function onAttachReferences() {
        console.log("onAttachReferences()");
        if (prevReferences === null)
            return;
        if (logicRule === null)
            return;

        // TODO: get prevReferences
        // TODO: set newly selected element to have
        // inference rule of logicRule

        logicRule = null;
        prevReferences = null;
    }

    // just create a node; the statement can be typed in by
    // the user, and the references can be chosen arbitrarily
    function onCreateNode() {
        console.log("onCreateNode()");
        // TODO: just create a node
    }

    $("#create-node").click(onCreateNode);
    $("#create-refs").on('submit', onCreateReferences);
    $("#attach-refs").click(onAttachReferences);
});
