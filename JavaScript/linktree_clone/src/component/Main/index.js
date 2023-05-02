import "./index.scss";
import DP from "../../Assets/dp.jpg";
 
const Main = () => {
  return (
    <div className="container">
      <div className="row">
        <h1 className="head row">
          <p>All my links!</p>
        </h1>
        <div className="image">
          <img src={DP} />
        </div>
        <div className="buttons">
          <button className="btn row btn2 btn-primary"> <a href="https://nikhilsharma.online/" target="_blank">Website</a></button>
        </div>
        <div className="buttons">
          <button className="btn row btn3 btn-primary"> <a href="https://www.linkedin.com/in/nikhilsharma26500/" target="_blank">LinkedIn</a></button>
        </div>
        <div className="buttons">
          <button className="btn row btn1 btn-primary"> <a href="https://github.com/nikhilsharma26500/" target="_blank">Github</a></button>
        </div>
        <div className="buttons">
          <button className="btn row btn4 btn-primary"> <a href="https://twitter.com/nikhil26500" target="_blank">Twitter</a></button>
        </div>
      </div>
    </div>
  );
};

export default Main;
