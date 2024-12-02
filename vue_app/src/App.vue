<template>
  <div id="app">
    <h1>Syarikat Takaful Brunei Darussalam</h1>
    <h3>Technical Programming Assessment</h3>

    <div class="form-container">
      <!-- Row with input and button inside columns -->
      <div class="form-row">
        <div class="form-col">
          <input 
            type="text" 
            v-model="apiKey" 
            placeholder="Enter your API key"
            required
          />
        </div>
        <div class="form-col">
          <button @click="fetchQuestions" :disabled="loading">
            {{ loading ? "Fetching..." : "Download Questions" }}
          </button>
        </div>
      </div>
    </div>

    <!-- Error message -->
    <p v-if="error" class="error-message">{{ error }}</p>

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
      apiKey: "",
      questions: [],
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchQuestions() {
      this.error = null;
      this.loading = true;

      try {
        const response = await axios.get("https://assessment.takafulbrunei.com/api/v1/download/questions", {
          headers: {
            "x-api-key": this.apiKey,  // API key passed in header
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
  justify-content: center;
  align-items: center;
}

.form-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;  /* Space between items */
  justify-content: center;  /* Center the items */
}

.form-col {
  display: flex;
  flex: 1;
  max-width: 300px;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 100%;  /* Make input fill its container */
}

button {
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;  /* Make button fill its container */
}

button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.questions-container {
  margin-top: 20px;
}

.error-message {
  color: #d9534f;
  margin-top: 10px;
}
</style>
