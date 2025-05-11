// src/services/auth.js
const API_BASE = 'http://127.0.0.1:8000';

export async function loginUser(email, password) {
    const response = await fetch(`${API_BASE}/utilizador/login/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || 'Erro ao fazer login.');
    }

    return data; // { access, refresh }
}

export async function refreshToken() {
    const refresh = localStorage.getItem('refreshToken');
    if (!refresh) throw new Error('Refresh token não encontrado.');

    const response = await fetch(`${API_BASE}/utilizador/refresh/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh }),
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || 'Erro ao atualizar token.');
    }

    localStorage.setItem('accessToken', data.access);
    return data.access;
}

// --------------------------------

const checkAdmin = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) return false;

    try {
        const response = await fetch('http://localhost:8000/check_admin/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        });
        const data = await response.json();
        return data.is_admin; // Retorna true se o utilizador for Admin
    } catch (error) {
        console.error('Error checking admin status:', error);
        return false;
    }
};

const checkCondutor = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) return false;

    try {
        const response = await fetch('http://localhost:8000/check_condutor/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        });
        const data = await response.json();
        return data.is_condutor; // Retorna true se o utilizador for Condutor
    } catch (error) {
        console.error('Error checking condutor status:', error);
        return false;
    }
};

const checkPassageiro = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) return false;

    try {
        const response = await fetch('http://localhost:8000/check_passageiro/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        });
        const data = await response.json();
        return data.is_passageiro; // Retorna true se o utilizador for Passageiro
    } catch (error) {
        console.error('Error checking passageiro status:', error);
        return false;
    }
};

export { checkAdmin, checkCondutor, checkPassageiro };

