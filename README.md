### Installing Dependencies

You can use the conan package manager to install dependencies.
(If you don't want to use conan, you can also install them on your own and pass them to CMake.)

If you choose to use the conan package manager, install it now, e.g.
~~~
$ pip3 install --user conan
~~~

Then install the dependencies:
~~~
$ cd build
$ conan install ..
~~~
This uses your default conan profile.
If you are not using Mac or want to use a different compiler, create a new profile by 
consulting the [official documentation](https://docs.conan.io/en/latest/reference/profiles.html).

On macOS, some conan packages have bugs in rpath support.
Indeed, conan's default approach seems to be to set the binary directory (`build/bin`) into
the `DYLD_LIBRARY_PATH` environment path.
(Also, somehow `bin` is preferred over `lib` by the Conan community...)
