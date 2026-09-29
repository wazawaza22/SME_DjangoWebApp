async function loadStudents() {
    // Get references to page elements
    const loadingMessage = document.getElementById("loading-message");
    const errorMessage = document.getElementById("error-message");
    const studentCount = document.getElementById("student-count");
    const tableBody = document.getElementById("student-table-body");

    try {
        // Set initial loading state
        loadingMessage.textContent = "Loading students...";
        errorMessage.textContent = "";

        // Fetch data from API
        const response = await fetch("/api/students/");

        // === NEW: Specific authentication error handling ===
        if (!response.ok) {
            if (response.status === 401) {
                throw new Error(
                    "Authentication required. Please log in."
                );
            }
            throw new Error(
                `HTTP error: ${response.status}`
            );
        }
        // === END: Authentication handling ===

        // Parse JSON response
        const data = await response.json();

        // Update total count
        studentCount.textContent = data.count;

        // Clear existing table rows
        tableBody.innerHTML = "";

        // Empty vs Populated
        if (data.students.length === 0) {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td colspan="5">
                    No Student records found.
                </td>
            `;
            tableBody.appendChild(row);
        } else {
            data.students.forEach(student => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${student.id}</td>
                    <td>${student.student_name}</td>
                    <td>${student.program}</td>
                    <td>${student.year_level}</td>
                    <td>${student.email}</td>
                `;
                tableBody.appendChild(row);
            });
        }

        // Done — clear loading message
        loadingMessage.textContent = "";

    } catch (error) {
        // Handle errors
        loadingMessage.textContent = "";
        errorMessage.textContent = error.message;
        console.error("Student loading error:", error);
    }
}

// Run the function when page loads
loadStudents();