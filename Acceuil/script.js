const body  = document.body;
const openSidebar = document.querySelector('#openSidebar');
const closeSidebar = document.querySelector('#closeSidebar');
const toggleTheme = document.querySelector('.toggle-theme');
const sidebar = document.querySelector('.main-sidebar');
const light = toggleTheme.children[0]
const dark = toggleTheme.children[1]
const percentage = document.querySelector('.percentage p')

openSidebar.addEventListener('click', ()=> {
    sidebar.style.left = '0%'
})

closeSidebar.addEventListener('click', ()=> {
    sidebar.style.left = '-100%'
})

toggleTheme.addEventListener('click', changeTheme)

function changeTheme() {
    if(body.classList.contains('dark-mode')) {
        lightMode()
    }else if (!body.classList.contains('dark-mode')) {
        darkMode()
    }

    if(window.matchMedia('(prefers-color-sheme: dark)').matches) {
        darkMode()
    }

    function lightMode () {
        body.classList.remove('dark-mode')
        light.classList.add('active')
        dark.classList.remove('active')
    }

    function darkMode() {
        body.classList.add('dark-mode')
        light.classList.remove('active')
        dark.classList.add('active')
    }

    /**
     * Pour les fitres
     */

}

const filterHeader = document.querySelector(".filter .filter-header")
const filterup = filterHeader.children[1]
const filterForm = document.querySelector(".filter .filter-form")


filterup.addEventListener('click', toggleFilt)

function toggleFilt(){
    if(filterForm.classList.contains("positionRight")) {
        filterForm.classList.remove("positionRight")
        filterup.classList.add("bi-caret-up-fill")
        filterup.classList.remove("bi-caret-down-fill")
    }else{
        filterForm.classList.add("positionRight")
        filterup.classList.remove("bi-caret-up-fill")
        filterup.classList.add("bi-caret-down-fill")
    }

}    