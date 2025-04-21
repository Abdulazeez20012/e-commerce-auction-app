document.addEventListener('DOMContentLoaded', () => {
    console.log('App initialized');

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            try {
                const formData = new FormData(form);
                const jsonData = Object.fromEntries(formData.entries()); // Ensure compatibility
                const response = await fetch(form.action, {
                    method: form.method,
                    body: JSON.stringify(jsonData),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    console.error('Error:', response.statusText);
                } else {
                    console.log('Form submitted successfully');
                }
            } catch (error) {
                console.error('Submission error:', error);
            }
        });
    });
});