    var v_fixed = false;

window.addEventListener('scroll', function (f_e) {
    c_topActionsSection = document.getElementById('id_top-actions-section');
    c_whiteSpace = document.createElement("div");
    c_whiteSpace.style = "width:100%;height:59.25px;margin:0;";
    c_whiteSpace.id = "id_topActionWhiteSpace"
    c_topActionPreviousSection = c_topActionsSection.previousElementSibling;
    if (window.scrollY >= 65) {
        c_topActionsSection.classList.add("c_buttons_fixed");
        if (!v_fixed) {
            c_topActionPreviousSection.appendChild(c_whiteSpace);
            v_fixed = true;
        }
    } else {
        c_topActionsSection.classList.remove("c_buttons_fixed");
        c_domWhiteSpace = document.getElementById('id_topActionWhiteSpace');
        c_domWhiteSpace.remove()
        v_fixed = false
    }
});