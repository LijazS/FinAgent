import React from "react";
import Header from "../components/Header.jsx";

const Dashboard = () => {

    return(
    <div className="w-full min-h-screen pt-12 left-0 right-0 bg-gray-900 text-white relative pt-20">
      <div className="w-full">
        <Header />
      </div>
                <div className="min-h-screen p-4 pt-6 bg-gray-700">
        <div className="grid grid-cols-4 gap-4 h-[90vh] ">
            
            {/* <!-- Left Column --> */}
            <div className="flex flex-col gap-4 col-span-2">
            <div className="bg-gray-500 rounded-lg shadow p-4 h-1/4">
                {/* Top small block */}
                Top Left
            </div>
            <div className="bg-gray-500 rounded-lg shadow p-4 h-3/4">
                {/* Bottom large block */}
                Bottom Left
            </div>
            </div>

            {/* Right Column */}
            <div className="flex flex-col gap-4 col-span-2">
            <div className="bg-gray-500 rounded-lg shadow p-4 h-1/2">
                {/* Top block */}
                Top Right
            </div>
            <div className="bg-gray-500 rounded-lg shadow p-4 h-1/2">
                {/* Bottom block */}
                Bottom Right
            </div>
            </div>

        </div>
        </div>
    </div>
    )

}

export default Dashboard;