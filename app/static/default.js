
  //$(document).ready();
  tableUrl = "";// e.g. "/students/"
search_filter = "";
  let selectedStudent = [];

  // Function to toggle the visibility of dropdown-blocks
  function toggleDropdown() {
    var dropdownBlocks = document.getElementById("dropdown-blocks");
    if (dropdownBlocks.classList.contains("hidden")) {
      dropdownBlocks.classList.remove("hidden");
      dropdownBlocks.classList.add("block");
    } else {
      dropdownBlocks.classList.remove("block");
      dropdownBlocks.classList.add("hidden");
    }
  }

  // Function to handle clicks on the document
  function documentClickHandler(event) {
    var dropdownBlocks = document.getElementById("dropdown-blocks");
    
    if (
      $("#dropdown-blocks").length > 0 &&
      event.target.id !== "dropdown-blocks" &&
      event.target.id !== "dropdown-button"
    ) {
      dropdownBlocks.classList.remove("block");
      dropdownBlocks.classList.add("hidden");
    }
    if (tableUrl=="/courses/" && $("#formDropdownBox").length > 0){
      var formDropdownBox = document.getElementById("formDropdownBox");
      
      if (
        event.target.id !== "formDropdownBox" &&
        event.target.id !== "formDropdownButton"
      ) {
        formDropdownBox.classList.remove("block");
        formDropdownBox.classList.add("hidden");
        document.getElementById("submit_button").classList.remove("hidden");
      }
    }
  }

  // Function to handle clicks on dropdown-blocks
  function dropdownBlocksClickHandler(event) {
    if (event.target.tagName === "BUTTON") {
      var dropdownButton = document.getElementById("dropdown-button");
      var textNode = Array.from(dropdownButton.childNodes).find(function (
        node
      ) {
        return node.nodeType === 3; // Filter text nodes
      });
      textNode.replaceWith(event.target.textContent);
search_filter = event.target.textContent.trim();
    }
console.log("search_filter");
    console.log(search_filter);
  }

  // Function to handle the click event on .btn-tabs elements
  function handleTabClick(event) {
    console.log("asdad");
    ["students", "courses", "colleges"].forEach(function (element) {
      document.getElementById(element).classList.remove("border-lime-400");
      document.getElementById(element).classList.add("border-transparent");
    });
    document.getElementById(event.target.id).classList.add("border-lime-400");
    document
      .getElementById(event.target.id)
      .classList.remove("border-transparent");

    console.log(tableUrl);
    tableUrl = "/" + event.target.id + "/";
    var content = document.getElementById("content");
search_filter = "";

    // Perform an AJAX load operation (you may need to use another approach like fetch or XMLHttpRequest)
fetch(tableUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.status}`);
        }
        return response.text();
      })
      .then((data) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, "text/html");
        if (doc.querySelector("parsererror")) {
          console.error("HTML validation error");
        } else {
          content.innerHTML = data;
          tablePick();
        }
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  }

  function searchTable(event){
    console.log("SEARCHTABLE");
    searchUrl = tableUrl + "search/";
    const csrfToken = document
      .querySelector("meta[name=csrf-token]")
      .getAttribute("content");
    const formData = {
      header: search_filter,
      search: document.getElementById("search-dropdown").value
    };
    var xhr = new XMLHttpRequest();
xhr.open("POST", searchUrl, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.onload = function () {
      document.getElementById("table-div").innerHTML = xhr.responseText;
    };
    xhr.send(JSON.stringify(formData));
    event.preventDefault();
    
    // xhr.open("POST", searchUrl, true);
    // xhr.setRequestHeader("Content-Type", "application/json");
    // xhr.setRequestHeader("X-CSRFToken", csrfToken);
    // xhr.onload = function () {
    // if (xhr.status === 200) {
    //     document.getElementById("table-div").innerHTML = xhr.responseText;
    // } else {
    //     console.error("Network response was not ok: " + xhr.status);
    // }
    // };
    // xhr.onerror = function () {
    // console.error("Request failed");
    // };
    // xhr.send(JSON.stringify(formData));
  }

  function toggleRow(event) {
    id = event.target
      .closest("tr")
      .querySelectorAll("td")[1]
      .textContent.trim();
    if (selectedStudent.includes(id)) {
      for (index in [0, 1, 2, 3, 4, 5, 6, 7]) {
        id = event.target.closest("tr").querySelectorAll("td")[index];
        id.classList.add("bg-gray-400", "text-white");
        id.classList.remove("bg-gray-200", "bg-gray-100");
      }
    } else {
      for (index in [0, 1, 2, 3, 4, 5, 6, 7]) {
        id = event.target.closest("tr").querySelectorAll("td")[index];
        id.classList.remove("bg-gray-400", "text-white");
        id.classList.add(index % 2 ? "bg-gray-100" : "bg-gray-200");
      }
    }
  }

  function toggleAllRow() {
    const table = document.getElementById("table-form"); // Get the table by its ID
    const rows = table.getElementsByTagName("tr");
    if (selectedStudent.length > 0) {
      for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");

        for (let j = 0; j < cells.length; j++) {
          cells[j].classList.add("bg-gray-400", "text-white");
          cells[j].classList.remove(j % 2 ? "bg-gray-100" : "bg-gray-200");
        }
      }
    } else {
      for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");

        for (let j = 0; j < cells.length; j++) {
          cells[j].classList.remove("bg-gray-400", "text-white");
          cells[j].classList.add(j % 2 ? "bg-gray-100" : "bg-gray-200");
        }
      }
    }
  }

  function allCheckbox(event) {
    ifAllChecked = event.target.checked ? true : false;
    document.querySelectorAll(".row-checkbox").forEach(function (tab) {
      tab.checked = ifAllChecked;
      if (
        ifAllChecked &&
        selectedStudent.indexOf(
          tab.closest("tr").querySelectorAll("td")[1].textContent.trim()
        )
      ) {
        selectedStudent.push(
          tab.closest("tr").querySelectorAll("td")[1].textContent.trim()
        );
      }
    });
    if (!ifAllChecked) selectedStudent = [];
    toggleAllRow();
    toggleDelete();
  }

  function toggleCheckBox(event) {
    const id = event.target
      .closest("tr")
      .querySelectorAll("td")[1]
      .textContent.trim();
    const index = selectedStudent.indexOf(id);
    if (index === -1) {
      selectedStudent.push(id);
    } else {
      selectedStudent.splice(index, 1);
    }
    toggleDelete();
    toggleRow(event);
  }

  function toggleDelete() {
    console.log("toggleDelete");
    const item = document.getElementById("delete_button");
    if (selectedStudent.length > 0) {
      item.disabled = false;
      item.classList.add(
        "bg-red-700",
        "border-red-700",
        "hover:bg-red-800",
        "focus:ring-4",
        "focus:outline-none",
        "focus:ring-red-300",
        "text-white"
      );
      item.classList.remove(
        "text-gray-200",
        "cursor-not-allowed",
        "bg-red-300",
        "border-red-300"
      );
    } else {
      item.disabled = true;
      item.classList.remove(
        "bg-red-700",
        "border-red-700",
        "hover:bg-red-800",
        "focus:ring-4",
        "focus:outline-none",
        "focus:ring-red-300",
        "text-white"
      );
      item.classList.add(
        "text-gray-200",
        "cursor-not-allowed",
        "bg-red-300",
        "border-red-300"
      );
    }
    //bg-red-700 border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300
    //bg-red-400 border-red-400
  }

  function closingDeleteDialog() {
    console.log("CLOSING DIALOG");
    const divToDelete = document.querySelector("[modal-backdrop]");
    document.getElementById("info-popup").classList.add("hidden");
    divToDelete.remove();
  }

  function deleteStudentDialog() {
    console.log("deleteStudentDialog called");
    dialog = document.getElementById("info-popup");
    dialog.classList.remove("hidden");
    dialog.classList.add("flex");
    dialog.setAttribute("role", "dialog");
    dialog.setAttribute("aria-modal", "true");

    const newDiv = document.createElement("div");

    // Customize the new div (e.g., add content, classes, styles)
    newDiv.setAttribute("modal-backdrop", "");
    newDiv.className =
      "bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40";

    // Append the new div to the body of the document
    document.body.appendChild(newDiv);
  }

  function deleteStudentCall() {
    console.log("tab @ deleteStudentCall:" + tableUrl);
    deleteUrl = tableUrl + "delete";
        const csrfToken = document
      .querySelector("meta[name=csrf-token]")
      .getAttribute("content");
    const formData = {
      list: selectedStudent,
    };
    console.log("formData is " + JSON.stringify(formData, null, 2));

    fetch(deleteUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.status}`);
        }
        return response.text();
      })
      .then((data) => {
        document.getElementById("content").innerHTML = data;
        addEntry("edit");
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });

    event.preventDefault();
  }

  function formDropdown(){
    console.log("formDropdown clicked");
    var formDropdownBlocks = document.getElementById("formDropdownBox");
    var submit_button = document.getElementById("submit_button");
    if (formDropdownBlocks.classList.contains("hidden")) {
      formDropdownBlocks.classList.remove("hidden");
      formDropdownBlocks.classList.add("block");
      submit_button.classList.add("hidden");
    } else {
      formDropdownBlocks.classList.remove("block");
      formDropdownBlocks.classList.add("hidden");
      submit_button.classList.remove("hidden");
    }
  }

  function formDropdownBlocksClickHandler(event) {
    console.log("dropdown chose");
    if (event.target.tagName === "BUTTON") {
      console.log("valid");
      var dropdownButton = document.getElementById("formDropdownButton");
      var textNode = Array.from(dropdownButton.childNodes).find(function (
        node
      ) {
        return node.nodeType === 3; // Filter text nodes
      });
      textNode.replaceWith(event.target.textContent);
    }
  }

  

  function tablePick() {
    console.log("tablePick function executed");

    // Add event listeners for the dropdown functionality
    document
      .getElementById("dropdown-button")
      .addEventListener("click", toggleDropdown);

    document.addEventListener("click", documentClickHandler);

    document
      .getElementById("header-checkbox")
      .addEventListener("click", allCheckbox);

    const checkboxes = document.getElementsByClassName("row-checkbox");

    for (let i = 0; i < checkboxes.length; i++) {
      checkboxes[i].addEventListener("click", toggleCheckBox);
    }

    document
      .getElementById("dropdown-blocks")
      .addEventListener("click", dropdownBlocksClickHandler);

    document
      .getElementById("delete_button")
      .addEventListener("click", deleteStudentDialog);
    document
          .getElementById("searchbar-form")
          .addEventListener("submit", searchTable);

    // document
    //   .getElementById("delete_button")
    //   .setAttribute("data-modal-target", "info-popup");
    // document
    //   .getElementById("delete_button")
    //   .setAttribute("data-modal-toggle", "info-popup");
    document
      .getElementById("proceed-to-delete")
      .addEventListener("click", deleteStudentCall);

    document
      .querySelectorAll(".remove-custom-backdrop")
      .forEach(function (tab) {
        if ($(this).attr("id") != "proceed-to-delete")
          tab.addEventListener("click", closingDeleteDialog);
      });

    document.getElementById("add_entry").addEventListener("click", function () {
      var addUrl = tableUrl + "/add/";
      var content = document.getElementById("content");

      // Perform an AJAX load operation (you may need to use another approach like fetch or XMLHttpRequest)
      var xhr = new XMLHttpRequest();
      xhr.onload = function () {
        content.innerHTML = this.responseText;
        addEntry("add");
      };
      xhr.open("GET", addUrl, true);
      xhr.send();
    });

    // Perform an AJAX load operation (you may need to use another approach like fetch or XMLHttpRequest)
    /*var xhr = new XMLHttpRequest();
      xhr.onload = function () {
        content.innerHTML = this.responseText;
        addEntry();
      };
      xhr.open("GET", addUrl, true);
      xhr.send();*/

    document.querySelector("table").addEventListener("click", function (event) {
      if (event.target.classList.contains("edit-btn")) {
        var editUrl = tableUrl + "edit/";
        var content = document.getElementById("content");

        const leftmostData = event.target
          .closest("tr")
          .querySelectorAll("td")[1]
          .textContent.trim();
        console.log("leftmostData:");
        console.log(leftmostData);

        var csrf_token = "{{ csrf_token() }}";
        var formData = {}
        if(tableUrl=="/students/"){
          formData = {
            id: leftmostData
          };
        }
        else if(tableUrl=="/courses/"){
          formData = {
            code: leftmostData
          };
        }
        console.log("formData is " + JSON.stringify(formData, null, 2));
        const request = new XMLHttpRequest();
        request.open("POST", editUrl);
        request.onload = function () {
          document.getElementById("content").innerHTML = this.responseText;
          addEntry("edit");
        };
        request.setRequestHeader("Content-type", "application/json");
        const csrfToken = document
          .querySelector("meta[name=csrf-token]")
          .getAttribute("content");
        request.setRequestHeader("X-CSRFToken", csrfToken);
        request.send(JSON.stringify(formData));
        event.preventDefault();
      }
    });
  }

  function addEntry(type) {
    url = tableUrl+ ((type == "add") ?  "add" : "edit") +tableUrl.slice(1, -2)+"/"; 
    console.log("addEntry function executed");

    if($("#id").length > 0){// /students/
      const input = document.getElementById("id");

      input.addEventListener("input", function (event) {
        const inputValue = event.target.value;

        // Remove any non-numeric characters and limit the length to 4
        const cleanedValue = inputValue.replace(/[^\d-]/g, "");

        event.target.value = cleanedValue;

        if (cleanedValue[cleanedValue.length - 1] == "-")
          event.target.value = cleanedValue.substring(0, cleanedValue.length - 1);
        else if (
          cleanedValue.length === 4 ||
          (cleanedValue.length == 5 &&
            cleanedValue[cleanedValue.length - 1] != "-")
        )
          event.target.value = cleanedValue + "-";
      });
    }
    if($("#formDropdownBox").length > 0){// /courses/
      console.log("formDropdownBox exists");
      document.addEventListener("click", function(event) {
        // if (!document.getElementById("formDropdownBox").classList.contains("hidden")) 
        //   formDropdown();
      });

      document
        .getElementById("formDropdownButton")
        .addEventListener("click", formDropdown);
        
      document
        .getElementById("formDropdownBox-choices")
        .addEventListener("click", formDropdownBlocksClickHandler);

    }


    document
      .getElementById("add-edit-form")
      .addEventListener("submit", function (event) {
        console.log("POST");
        var csrf_token = "{{ csrf_token() }}";

        var formData = {};
        if (tableUrl=="/students/"){
          formData = {
            id: $("#id").val(),
            firstname: $("#firstname").val(),
            lastname: $("#lastname").val(),
            course: $("#course").val(),
            year: $("#year").val(),
            gender: $("#gender").val(),
          }
        }
        if (tableUrl=="/courses/"){
          formData = {
            code: $("#code").val(),
            name: $("#name").val(),
            college: $("#formDropdownButton").contents().filter(function() {            
                  return this.nodeType === 3; // Filter text nodes
              }).text().trim(),
          }
        }
        console.log("formData is " + JSON.stringify(formData, null, 2));
        const request = new XMLHttpRequest();
        request.open("POST", url);
        request.onload = () => {
          console.log("POST SUCCESSFUL");
          const element = document.getElementById(tableUrl.slice(1, -1));

          // Check if the element exists (not null)
          if (element) {
            // Programmatically trigger a click event
            element.click();
          }
        };
        request.setRequestHeader("Content-type", "application/json");
        const csrfToken = document
          .querySelector("meta[name=csrf-token]")
          .getAttribute("content");
        request.setRequestHeader("X-CSRFToken", csrfToken);
        request.send(JSON.stringify(formData));
        event.preventDefault();
      });
  }

  // Add event listeners to .btn-tabs elements
  document.querySelectorAll(".btn-tabs").forEach(function (tab) {
    tab.addEventListener("click", handleTabClick);
  });

  $(document).ready(function () {
    document.getElementById("students").click();
  });