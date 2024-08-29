document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".btn-delete");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            const confirmDelete = confirm("Êtes-vous sûr de vouloir supprimer cet element ?");
            if (!confirmDelete) {
                event.preventDefault(); // Prevent the default action if the user cancels
            } else {
                // Code to delete the student goes here
                alert("element supprimé!"); // Just for demonstration purposes
            }
        });
    });
});
