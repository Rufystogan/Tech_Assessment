<template>
  <div id="app">
    <h1>Syarikat Takaful Brunei Darussalam</h1>
    <h3>Technical Programming Assessment
      Instructions</h3>

    <!-- Form for API Key -->
    <form @submit.prevent="getApiKey" class="form-container">
      <input 
        type="text" 
        v-model="name" 
        placeholder="Name" 
        required 
      />
      <input 
        type="email" 
        v-model="email" 
        placeholder="Email" 
        required 
      />
      <button type="submit" :disabled="loading">
        {{ loading ? "Loading..." : "Get API Key" }}
      </button>
    </form>

    <!-- Error message -->
    <p v-if="error" class="error-message">{{ error }}</p>

    <!-- API Key Display -->
    <div v-if="apiKey" class="api-key-container">
      <h2>Your API Key:</h2>
      <p class="api-key">{{ apiKey }}</p>
      <button @click="fetchQuestions" :disabled="loading">
        {{ loading ? "Fetching..." : "Download Questions" }}
      </button>
    </div>

    <!-- Questions List -->
    <div v-if="questions.length > 0" class="questions-container">
      <h3>Questions:</h3>
      <ul>
        <li v-for="(question, index) in questions" :key="index">
          {{ question }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      name: "",
      email: "",
      apiKey: "",
      questions: [],
      loading: false,
      error: null,
    };
  },
  methods: {
    async getApiKey() {
      // Reset error and set loading state
      this.error = null;
      this.loading = true;

      // Input validation
      if (!this.name || !this.email) {
        this.error = "Name and email are required.";
        this.loading = false;
        return;
      }

      try {
        const response = await axios.post("http://127.0.0.1:5000/api/v1/candidate/", {
          name: this.name,
          email_address: this.email,
        });
        this.apiKey = response.data.api_key;
      } catch (error) {
        this.error = "Error fetching API key. Please try again.";
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
    async fetchQuestions() {
      // Reset error and set loading state
      this.error = null;
      this.loading = true;

      try {
        const response = await axios.get("http://127.0.0.1:5000/api/v1/download/questions", {
          headers: {
            "x-api-key": this.apiKey,
          },
        });
        this.questions = response.data.questions;
      } catch (error) {
        this.error = "Error fetching questions. Please try again.";
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
/* Styling */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
  color: #333;
}

#app {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

input[type="text"],
input[type="email"] {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.api-key-container {
  margin-top: 20px;
  text-align: center;
}

.api-key {
  font-weight: bold;
  color: #007bff;
}

.questions-container {
  margin-top: 20px;
}

.error-message {
  color: #d9534f;
  margin-top: 10px;
}
</style>
