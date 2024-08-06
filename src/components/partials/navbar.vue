<template>
    
    <div class="navbar ps-3 pe-3">
        <div class="navbar-brand">
            Friends Talk
        </div>
        <div class="search">
            <span class="search-icon"><font-awesome-icon :icon="['fas', 'magnifying-glass']" /></span>
            <input type="text" placeholder="Search Friends" >
        </div>
        <ul>
               <li><a href=""><font-awesome-icon :icon="['fas', 'message']" /><span class="count">9+</span></a> </li>
               <li><a href=""><font-awesome-icon :icon="['fas', 'bell']" /><span class="count">9+</span></a></li>
               <li><a href=""><img src="https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg" class="rounded-circle" alt=""> <span class="dropdown-icon"><font-awesome-icon :icon="['fas', 'chevron-down']" /></span></a></li>
        </ul>
    
    </div>
</template>
<script>
export default {
    name:"navbar_section"
}
</script>
<style scoped>
.navbar{
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    height: 75px;
    display: flex;
    align-items: center;


}
.navbar-brand{
    height: 100%;
}

ul{
 
    display:flex;
    list-style: none;
    align-items: center;
    gap: 30px;
    height: 100%;
  
}
img{
    width: 40px;
    height: 40px;
}
ul  li a{
    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.1rem;
    color: black;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    background: #f2f2f2;
    text-decoration: none;
    position: relative;
}
.search{
    position:relative;
    height: 100%;
}
.search input{
    height:45px;
    width: 25rem;
    border-radius:  45px;
    outline:none;
    border: none;
    background: #f2f2f2;
    padding-left: 3rem;
}
.search-icon{
    position: absolute;
    top:calc(22.5px - 0.6rem);
    left: 0.8rem;
    color: #636c72;
}
.count{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: red;
    font-size: 0.7rem;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    position: absolute;
    top: -5px;
    right: -5px;
}
.dropdown-icon{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #f2f2f2;
    font-size: 0.7rem;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #636c72;
    position: absolute;
    bottom: -5px;
    right: -5px;
}
</style>