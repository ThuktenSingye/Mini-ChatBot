<h1>LangChain: Document-based Question Answering with Chat Interface</h1>
<p>LangChain is a Python package that facilitates document-based question answering using a conversational interface. It leverages various natural language processing tools and models to enable users to interactively query information from documents.</p>

<h2>Features:</h2>
<ul>
  <li><strong>PDF Parsing:</strong> LangChain can extract text from PDF documents, making it easier to work with large amounts of textual data.</li>
  <li><strong>Text Splitting:</strong> It employs a character-based text splitter to chunk the text into manageable pieces, ensuring efficient processing without exceeding token size limits.</li>
  <li><strong>Embeddings and Vectorization:</strong> LangChain utilizes OpenAI embeddings to convert text into numerical vectors, enabling efficient similarity search and document retrieval.</li>
  <li><strong>Question Answering Chain:</strong> The package provides a question-answering chain that processes user queries and returns relevant information from the input documents.</li>
  <li><strong>Chat Interface:</strong> LangChain offers a user-friendly chat interface, allowing users to interact with the question-answering system in a conversational manner.</li>
</ul>

<h2>Usage:</h2>
<ol>
  <li>Provide the path to the PDF document containing the information you want to query.</li>
  <li>Run the provided script, which extracts text from the PDF, splits it into manageable chunks, and prepares it for processing.</li>
  <li>Interact with the chat interface by entering your questions. LangChain will search the documents for relevant information and provide answers in real-time.</li>
</ol>

<h2>Dependencies:</h2>
<ul>
  <li>PyPDF2</li>
  <li>langchain</li>
  <li>langchain_community</li>
  <li>langchain_openai</li>
  <li>langchain_core</li>
  <li>typing_extensions</li>
</ul>
