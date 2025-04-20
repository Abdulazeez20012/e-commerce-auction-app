document.addEventListener('DOMContentLoaded', () => {
    console.log('App initialized');

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch(form.action, {
                method: form.method,
                body: JSON.stringify(Object.fromEntries(formData)),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        });
    });
});