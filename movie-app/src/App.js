import React from 'react';
import './App.css';
  
function App() {
    return (
        <div>
            <nav class="navbar background">
                <ul class="nav-list">
                    <div class="title">
                        <h1>Movie Recommendation</h1>
                    </div>
                    <li><a href="www.google.com">Current List</a></li>
                    <li><a href="www.google.com">Past List</a></li>
                    <li><a href="www.google.com">Future List</a></li>
                    <li><a href='www.google.com'>Filter</a></li>
                </ul>
  
                <div class="rightNav">
                    <input type="text" name="search" id="search" />
                    <button class="btn btn-sm">Search</button>
                </div>
            </nav>
  
            <section class="section">
                <div class="box-main">
                    <div class="firstHalf">
                        <h1 class="text-big">
                            
                        </h1>
                        <p class="text-small">
                           
                        </p>
                    </div>
                </div>
            </section>
            <section class="section">
                <div class="box-main">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                           
                        </h1>
                        <p class="text-small">
                            
                        </p>
                    </div>
                </div>
            </section>
            <section class="section">
                <div class="box-main">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            
                        </h1>
                        <p class="text-small">
                            
                        </p>
                    </div>
                </div>
            </section>
            <section class="section">
                <div class="box-main">
                    <div class="secondHalf">
                        <h1 class="text-big" id="program">
                            
                        </h1>
                        <p class="text-small">
                            
                        </p>
                    </div>
                </div>
            </section>
            <footer className="footer">
                <p className="text-footer">
                    
                </p>
            </footer>
        </div>
    )
}
  
export default App